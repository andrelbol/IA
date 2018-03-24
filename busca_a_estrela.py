from model.Transition import Transition
from model.Node import Node

def setup_nodes():
    nodes = []
    nodes.append(Node("Arad", 366))
    nodes.append(Node("Timisoara", 329))
    nodes.append(Node("Zerind", 374))
    nodes.append(Node("Fagaras", 176))
    nodes.append(Node("Sibiu", 253))
    nodes.append(Node("Rimnicu Vilcea", 193))
    nodes.append(Node("Pitesi", 10))
    nodes.append(Node("Bucharest", 0))
    nodes.append(Node("Oradea", 380))
    nodes.append(Node("Craiova", 160))
    return nodes

def get_node_by_value(value, nodes):
    for node in nodes:
        if(node.value == value):
            return node

def setup_initial_transitions(nodes):
    transitions = []

    transitions.append(Transition(get_node_by_value("Arad", nodes), get_node_by_value("Zerind", nodes), 75))
    transitions.append(Transition(get_node_by_value("Arad", nodes), get_node_by_value("Timisoara", nodes), 118))
    transitions.append(Transition(get_node_by_value("Arad", nodes), get_node_by_value("Sibiu", nodes), 140))
    transitions.append(Transition(get_node_by_value("Zerind", nodes), get_node_by_value("Arad", nodes), 75))
    transitions.append(Transition(get_node_by_value("Zerind", nodes), get_node_by_value("Oradea", nodes), 71))
    transitions.append(Transition(get_node_by_value("Sibiu", nodes), get_node_by_value("Rimnicu Vilcea", nodes), 80))
    transitions.append(Transition(get_node_by_value("Sibiu", nodes), get_node_by_value("Fagaras", nodes), 99))
    transitions.append(Transition(get_node_by_value("Sibiu", nodes), get_node_by_value("Oradea", nodes), 151))
    transitions.append(Transition(get_node_by_value("Sibiu", nodes), get_node_by_value("Arad", nodes), 140))
    transitions.append(Transition(get_node_by_value("Timisoara", nodes), get_node_by_value("Arad", nodes), 118))
    transitions.append(Transition(get_node_by_value("Oradea", nodes), get_node_by_value("Zerind", nodes), 75))
    transitions.append(Transition(get_node_by_value("Oradea", nodes), get_node_by_value("Sibiu", nodes), 151))
    transitions.append(Transition(get_node_by_value("Fagaras", nodes), get_node_by_value("Bucharest", nodes), 211))
    transitions.append(Transition(get_node_by_value("Fagaras", nodes), get_node_by_value("Sibiu", nodes), 99))
    transitions.append(Transition(get_node_by_value("Rimnicu Vilcea", nodes), get_node_by_value("Pitesi", nodes), 97))
    transitions.append(Transition(get_node_by_value("Rimnicu Vilcea", nodes), get_node_by_value("Sibiu", nodes), 80))
    transitions.append(Transition(get_node_by_value("Rimnicu Vilcea", nodes), get_node_by_value("Craiova", nodes), 146))
    transitions.append(Transition(get_node_by_value("Pitesi", nodes), get_node_by_value("Bucharest", nodes), 101))
    transitions.append(Transition(get_node_by_value("Pitesi", nodes), get_node_by_value("Rimnicu Vilcea", nodes), 97))
    transitions.append(Transition(get_node_by_value("Pitesi", nodes), get_node_by_value("Craiova", nodes), 138))
    transitions.append(Transition(get_node_by_value("Craiova", nodes), get_node_by_value("Rimnicu Vilcea", nodes), 145))
    transitions.append(Transition(get_node_by_value("Craiova", nodes), get_node_by_value("Pitesi", nodes), 138))
    return transitions

def test_objective(current_node, nodes):
    objective = get_node_by_value("Bucharest", nodes)
    return current_node == objective

def get_shortest_transition(transitions):
    best_transition = transitions[0]
    for transition in transitions:
        if(best_transition.weight > transition.weight):
            best_transition = transition
    return best_transition

def remove_walked_path(transitions, walked_path):
    # Remove the walked transition, and the inverse of it (you can't go back)
    aux_list = list(transitions) # Need to make a copy because will change the original
    for transition in aux_list:
        if((transition.to == walked_path.to and transition.current == walked_path.current)
            or (transition.to == walked_path.current and transition.current == walked_path.to)):
            transitions.remove(transition)

def print_transitions_array(transitions):
    # Just a debug function
    for transition in transitions:
        print(transition)

def step(current_node, learned_transitions, all_transitions):
    # Successor function
    node_avaiable_transitions = current_node.get_avaiable_transitions(all_transitions)
    for transition in node_avaiable_transitions:
        aux_transition = transition
        aux_transition.weight += (aux_transition.current.already_walked + aux_transition.to.heuristic)
        learned_transitions.append(aux_transition)
    
    next_transition = get_shortest_transition(learned_transitions)
    remove_walked_path(all_transitions, next_transition) # Remove so it doesn't count in next iteration
    remove_walked_path(learned_transitions, next_transition) # Remove so it doesn't count in next iteration
    return next_transition

def main():
    nodes = setup_nodes()
    transitions = setup_initial_transitions(nodes)
    learned_transitions = []
    walked_transitions = []

    # Start at Arad
    current_node = get_node_by_value("Arad", nodes)

    # Steps
    while(not(test_objective(current_node, nodes))):
        new_transition = step(current_node, learned_transitions, transitions)
        walked_transitions.append(new_transition)
        current_node = new_transition.to
        current_node.already_walked = new_transition.weight - current_node.heuristic
        print("\n")
        print_transitions_array(walked_transitions)

main()