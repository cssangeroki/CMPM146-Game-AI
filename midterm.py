class Game:

    def __init__(self, *params): pass

    def legal_actions(self): pass

    def apply_move(self, move): pass

    def is_terminal(self): pass

    def score(self): pass


class Node:

    def __init__(self, last_action, action_list, parent_node=None):

        self.child_nodes = {}
        self.score = 0
        self.visits = 0
        self.parent = parent_node
        self.parent_action = last_action
        self.untried_actions = action_list

    def ucb(child_node):

        parent_node = child_node.parent
        return (child_node.score/child_node.visits) + \
            sqrt(log(parent_node.visits)/child_node.visits)

    def traverse_nodes(node, game, bot_identity):

        while not game.is_terminal() and not node.untried_actions:
            child_node = max(node.child_nodes.values(), key=ucb)
            game.apply_move(child_node.parent_action)
            node = child_node
        return node

    def backpropagate(score, node):

        while node:
            node.score += score
            node.visits += 1
            node = node.parent
