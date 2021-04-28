import sys
sys.path.insert(0, '../')
from planet_wars import issue_order

from math import ceil


def attack_weakest_enemy_planet(state):
    # (1) If we currently have a fleet in flight, abort plan.
    if len(state.my_fleets()) >= 1:
        return False

    # (2) Find my strongest planet.
    strongest_planet = max(state.my_planets(), key=lambda t: t.num_ships, default=None)

    # (3) Find the weakest enemy planet.
    weakest_planet = min(state.enemy_planets(), key=lambda t: t.num_ships, default=None)

    if not strongest_planet or not weakest_planet:
        # No legal source or destination
        return False
    else:
        # (4) Send half the ships from my strongest planet to the weakest enemy planet.
        return issue_order(state, strongest_planet.ID, weakest_planet.ID, strongest_planet.num_ships / 2)


def spread_to_weakest_neutral_planet(state):
    # (1) If we currently have a fleet in flight, just do nothing.
    if len(state.my_fleets()) >= 1:
        return False

    # (2) Find my strongest planet.
    strongest_planet = max(state.my_planets(), key=lambda p: p.num_ships, default=None)

    # (3) Find the weakest neutral planet.
    weakest_planet = min(state.neutral_planets(), key=lambda p: p.num_ships, default=None)

    if not strongest_planet or not weakest_planet:
        # No legal source or destination
        return False
    else:
        # (4) Send half the ships from my strongest planet to the weakest enemy planet.
        return issue_order(state, strongest_planet.ID, weakest_planet.ID, strongest_planet.num_ships / 2)


def consolidate_ships(state):
    """
        Gathers ships from lower tier planets to higher tier planets

        Tries to keep a base level defense proportional to planet tier
    """

    # Keep a base of X times the planet's production in ships
    modifier_planet_defense = 15
    # X times the planet's production is an excess of ships
    modifier_planet_spares  = 20

    # Check we have more than one fleet to consider
    player_planets = sorted(state.my_planets(), key=lambda t: t.growth_rate)

    if len(player_planets) < 2:
        return False

    player_home = player_planets[-1]
    player_planets = player_planets[:-1]

    # If a planet has an enemy fleet attacking it, then keep ships on planet
    planets_under_attack = set( [fleet.destination_planet for fleet in state.enemy_fleets() ] )

    # Check all non-home owned planets for spare ships starting with the lowest tier
    for planet in player_planets:
        if planet.ID not in planets_under_attack and (planet.growth_rate * modifier_planet_spares) < planet.num_ships:
            transfer_size = planet.num_ships - (planet.growth_rate * modifier_planet_defense)

            return issue_order(state, planet.ID, player_home.ID, transfer_size)

    # No planet has spare ships
    return False


def capture_neighbors(state):
    """
        Focus on securing close planets

    """

    # Distance is how far from home_planet to consider
    modifier_neighbor_distance   = 20
    # How much are more productive planets valued; how much more is a 2-ship planet prefered over a 1-ship
    modifier_neighbor_production = 2

    # How much to consider a planet's defense
    # A higher value means that we need to outnumber them by more before considering
    modifier_neighbor_defense    = 1.3

    # How much more to prioritize planets that are owned by an enemy
    modifier_neighbor_enemy      = 1.3

    home_planet = max(state.my_planets(), key=lambda t: t.num_ships)

    if not home_planet:
        return False


    # Check for any fleets that are already capturing
    targeted_planets = set( [ fleet.destination_planet for fleet in state.my_fleets() ] )
    enemy_targeted_planets = set( [ fleet.destination_planet for fleet in state.enemy_fleets() ] )
    if enemy_targeted_planets:
        targeted_planets = targeted_planets | enemy_targeted_planets


    def planet_val(planet):
        # Can it be captured with our fleet?
        if (modifier_neighbor_defense * planet.num_ships) > home_planet.num_ships:
            return -1

        # Larger distances, less desireable
        dist_val = modifier_neighbor_distance / state.distance(home_planet.ID, planet.ID)
        prod_val = modifier_neighbor_production * planet.growth_rate

        # Defense of planets when ships would arrive at location
        defs_val = home_planet.num_ships / (expected_fleet(state, home_planet, planet) * modifier_neighbor_defense)

        # TODO: maybe some logic to perfer enemies that are weaker/stronger?
        enem_val = modifier_neighbor_enemy

        return (dist_val + prod_val + defs_val + enem_val)

    # list of neighbors sorted by decreasing planet value
    neighbor_planets = [ planet for planet in state.not_my_planets() if planet.ID not in targeted_planets ]
    neighbor_planets = sorted(neighbor_planets, key=lambda t: planet_val(t), reverse=True)

    for neighbor in neighbor_planets:
        garrison = 0
        required_fleet = expected_fleet(state, home_planet, neighbor) + ceil(state.distance(home_planet.ID, neighbor.ID))

        if enemy_targeted_planets and home_planet.ID in enemy_targeted_planets:
            garrison = sum([ fleet.num_ships for fleet in state.enemy_fleets() if fleet.destination_planet == home_planet.ID ])

        if home_planet.num_ships > required_fleet + garrison:
            return issue_order(state, home_planet.ID, neighbor.ID, required_fleet)
        else:
            return False

    return False

def coup_de_grace(state):
    """
        Finish enemy when they are left with a single planet

    """
    enemy_planet = any(state.enemy_planets())

    # (1) If enemy has planet, then attack with neighbors
    if enemy_planet:
        local_friendlies = sorted(state.my_planets(), key=lambda t: state.distance(enemy_planet.ID, t.ID))
        for local in local_friendlies:
            # keep back as many ships as it would take to repel that planet attacking back
            garrison = expected_fleet(state, enemy_planet, local) + 1
            if local.num_ships - garrison > expected_fleet(state, local, enemy_planet) + 1:
                return issue_order(state, local.ID, enemy_planet.ID, local.num_ships - garrison)

        # No local planet can attack safely
        return False

    # (2) If enemy has no planet, check for their fleets, reinforce planets being targeted

    enemy_fleets = sorted(state.enemy_fleets(), key=lambda f: f.num_ships, reverse=True)
    if enemy_fleets:
        enemy_targets = set([ f.destination_planets for f in enemy_fleets ])

        for fleet in enemy_fleets:
            target_planet = state.planets[fleet.destination_planet]
            # Check if target will survive
            target_defence = target_planet.num_ships + (target_planet.growth_rate * fleet.turns_remaining)
            if target_defence >= fleet.num_ships:
                continue

            # Target will fall, so send support
            local_friendlies = sorted(state.my_planets(), key=lambda f: state.distance(target_planet.ID, t.ID), reverse=True)
            # remove target from list
            local_friendlies = local_friendlies[1:]

            for local in local_friendlies:
                if local.ID not in enemy_targets:
                    return issue_order(state, local.ID, target_planet.ID, local.num_ships -1)

    # No planets will be lost
    return False

#### HELPER FUNCTIONS ####

# Calculates how many ships will encountered by a friendly fleet departing from source at destination
def expected_fleet(state, source, destination):
    # Only captured planets will grow in strength
    travel_growth = 0
    if destination.owner != 0:
        travel_growth = state.distance(source.ID, destination.ID) * destination.growth_rate

    return (destination.num_ships + travel_growth)
