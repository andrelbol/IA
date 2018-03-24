class Node:

    def __init__(self, value, heuristic):
        self.value = value
        self.heuristic = heuristic
        self.already_walked = 0

    def get_avaiable_transitions(self, transitions):
        result = []
        for transition in transitions:
            if(transition.current.value == self.value):
                result.append(transition)
        return result

    @staticmethod
    def get_node_by_value(value, nodes):
        for node in nodes:
            if(node.value == value):
                return node

    def __str__(self):
        return self.value