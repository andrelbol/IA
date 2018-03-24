class Node:

    def __init__(self, value, heuristic):
        self.value = value
        self.heuristic = heuristic

    def get_adjacent_nodes_transitions(self, transitions):
        result = []
        for transition in transitions:
            if(transition.current.value == self.value):
                result.append(transition)
        return result

    def __str__(self):
        return self.value

class Transition:

    def __init__(self, current, to, weight):
        self.current = current
        self.to = to
        self.weight = weight

    def __str__(self):
        return "From: " + self.current.value + ", To: " + self.to.value + ", weight: " + str(self.weight)

def setup_nodes():
    nodes = []
    nodes.append(Node("Arad", 366))
    nodes.append(Node("Oradea", 380))
    nodes.append(Node("Zerind", 374))
    nodes.append(Node("Iasi", 226))
    return nodes

def get_node_by_value(value, nodes):
    for node in nodes:
        if(node.value == value):
            return node

def setup_initial_transitions():
    transitions = []
    nodes = setup_nodes()

    transitions.append(Transition(get_node_by_value("Arad", nodes), get_node_by_value("Zerind", nodes), 75))
    transitions.append(Transition(get_node_by_value("Zerind", nodes), get_node_by_value("Arad", nodes), 75))
    transitions.append(Transition(get_node_by_value("Zerind", nodes), get_node_by_value("Oradea", nodes), 71))
    transitions.append(Transition(get_node_by_value("Oradea", nodes), get_node_by_value("Zerind", nodes), 75))

    return transitions

def main():
    transitions = setup_initial_transitions()
    for t in transitions:
        print(t)
    return True

main()