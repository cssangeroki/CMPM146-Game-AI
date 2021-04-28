import copy
from planet_wars import issue_order
import sys
sys.path.insert(0, '../')


def attack_weakest_enemy_planet(state):
    # (1) If we currently have a fleet in flight, abort plan.
    if len(state.my_fleets()) >= 1:
        return False

    # (2) Find my strongest planet.
    strongest_planet = max(
        state.my_planets(), key=lambda t: t.num_ships, default=None)

    # (3) Find the weakest enemy planet.
    weakest_planet = min(state.enemy_planets(),
                         key=lambda t: t.num_ships, default=None)

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
    strongest_planet = max(
        state.my_planets(), key=lambda p: p.num_ships, default=None)

    # (3) Find the weakest neutral planet.
    weakest_planet = min(state.neutral_planets(),
                         key=lambda p: p.num_ships, default=None)

    if not strongest_planet or not weakest_planet:
        # No legal source or destination
        return False
    else:
        # (4) Send scaling number of ships from my strongest planet to the weakest enemy planet.
        return issue_order(state, strongest_planet.ID, weakest_planet.ID, weakest_planet.num_ships * (1 + (1/strongest_planet.growth_rate)))


def greedy_neutral_planet_spread(state):
    ##############################################################################
    # 1. Greedily search for best neutral planets and send fleet to conquer.
    # 2. After enemy captures a base, send fleet to capture planet
    ##############################################################################

    planetArray = []
    for i in state.neutral_planets:
        if not any(fleet.destination_planet == i.ID for fleet in state.my_fleets()):
            planetArray.append()

    planetArray.sort(key=lambda p: p.num_ships * (1 + 1/p.growth_rate))
    target_planets = iter(planetArray)

    while not StopIteration:
        i = 0
        myPlanets = state.my_planets()
        myPlanets.sort(key=lambda p: p.num_ships * (1 + 1/p.growth_rate))
        fleet = []
        shipsToSend = 0

        ####################################################################
        # Best Planets will supply ships and send to conquer
        ####################################################################
        while i < 3 and i < len(fleet):
            fleet.append(myPlanets[i])
            shipsToSend += myPlanets[i].num_ships*(1/2)
            i += 1
#            logging.info(i)
        fleet.sort(key=lambda p: distance(p, myPlanets))
        fleetIter = iter(fleet)
        nextPlanet = next(fleetIter)
        required_ships = myPlanets.num_ships + 1
        j = 0

        ################################################################
        # Send Half Ships to attack from conquered planets
        ################################################################

        for j in range(5):
            squad = nextPlanet.num_ships / 2
            issue_order(state, nextPlanet.ID,
                        myPlanets.ID, squad)
            nextPlanet = next(myPlanets)
            j += 1


def steal_planets(state):

    while not StopIteration:

        past_enemy_planets = []
        current_enemy_planets = state.enemy_planets()

        if past_enemy_planets:
            if len(current_enemy_planets) != len(past_enemy_planets):
                difference = [i for i in current_enemy_planets +
                              past_enemy_planets if i not in current_enemy_planets or i not in past_enemy_planets]

        past_enemy_planets = copy.deepcopy(current_enemy_planets)

        #############################################################
        # Attack recently conquered planet
        #############################################################
        my_troops = sorted(state.my_planets(),
                           key=lambda t: state.distance(difference[0].ID, t.ID))
        for i in my_troops:
            issue_order(state, i.ID, difference[0].ID, i.num_ships / 2)
