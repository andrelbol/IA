from model.Transition import Transition
from model.Node import Node

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

def setup_initial_transitions(nodes):
    transitions = []

    transitions.append(Transition(get_node_by_value("Arad", nodes), get_node_by_value("Zerind", nodes), 75))
    transitions.append(Transition(get_node_by_value("Zerind", nodes), get_node_by_value("Arad", nodes), 75))
    transitions.append(Transition(get_node_by_value("Zerind", nodes), get_node_by_value("Oradea", nodes), 71))
    transitions.append(Transition(get_node_by_value("Oradea", nodes), get_node_by_value("Zerind", nodes), 75))

    return transitions

def test_objective(current_node, nodes):
    objective = get_node_by_value("Bucharest", nodes)
    return current_node == objective

def get_shortest_transition(transitions):
    best_transition = learned_transitions[0]
    for transition in learned_transitions:
        if(best_transition.weight > transition.weight):
            best_transition = transition
    return best_transition

def step(current_node, already_walked, learned_transitions):
    node_avaiable_transitions = current_node.get_avaiable_transitions()
    for transition in node_avaiable_transitions:
        aux_transition = transition
        aux_transition.weight += (already_walked + aux_transition.to.heuristic)
        learned_transitions.append(aux_transition)
    
    next_transition = get_shortest_transition(learned_transitions)
    current_node = next_transition.to
    already_walked += (next_transition.weight - next_transition.to.heuristic) # Heuristic doesn't count in way already walked
    learned_transitions.remove(next_transition) # Remove so it doesn't count in next iteration
    # TODO(@andre): finish this function and test it
    


    



def main():
    nodes = setup_nodes()
    transitions = setup_initial_transitions(nodes)
    learned_transitions = []
    already_walked = 0

    # Start at Arad
    current_node = get_node_by_value("Arad", nodes)

    # while(not(test_objective(current_node, nodes))):
    #     current_node = step()
    #     return True
    

main()