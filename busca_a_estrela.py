class Node:
    def get_adjacent_nodes_transitions(self, transitions):
        result = []
        for transition in transitions:
            if(transition.current.value == self.value):
                result.append(transition)
        return result

    def __init__(self, value, heuristic):
        self.value = value
        self.heuristic = heuristic

    def __str__(self):
        return self.value

class Transition:
    def __init__(self, current, to, weight):
        self.current = current
        self.to = to
        self.weight = weight

    def __str__(self):
        return "From: " + self.current + ", To: " + self.to + ", weight: " + str(self.weight)

def search(origin, destination, transitions):

    current_node = origin
    # Starting search
    available_transitions = origin.get_adjacent_nodes(transitions)

    cheapest_transition = Transition(None, None, 0);
    for(transition in available_transitions):
        if(cheapest_transition.weight > transition.weight):
            cheapest_transition = transition
    current_node = cheapest_transition.to
    current_node.trace = cheapest_transition.weight


    # Step
    # Andar um nó
    # Adiciono os adjacentes aos disponíveis



arad = Node("Arad", 366)
oradea = Node("Oradea", 380)
zerind = Node("Zerind", 374)
iasi = Node("Iasi", 226)

transitions = []
transitions.append(Transition(arad, zerind, 75))
transitions.append(Transition(zerind, arad, 75))
transitions.append(Transition(zerind, oradea, 71))
transitions.append(Transition(oradea, zerind, 75))

tmp = arad.get_adjacent_nodes(transitions)
