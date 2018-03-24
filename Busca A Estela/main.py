from model.Transition import Transition
from model.Node import Node
from init_data import setup_nodes, setup_initial_transitions

def objective_function(current_node, nodes):
    # End at Bucharest
    objective = Node.get_node_by_value("Bucharest", nodes)
    return current_node == objective

def step_function(current_node, learned_transitions, all_transitions):
    # Successor function
    node_avaiable_transitions = current_node.get_avaiable_transitions(all_transitions)
    for transition in node_avaiable_transitions:
        aux_transition = transition
        aux_transition.weight += (aux_transition.current.already_walked + aux_transition.to.heuristic)
        learned_transitions.append(aux_transition)
    
    next_transition = Transition.get_shortest_transition(learned_transitions)
    Transition.remove_walked_path(all_transitions, next_transition) # Remove so it doesn't count in next iteration
    Transition.remove_walked_path(learned_transitions, next_transition) # Remove so it doesn't count in next iteration
    return next_transition

def main():
    nodes = setup_nodes()
    transitions = setup_initial_transitions(nodes)
    learned_transitions = []
    walked_transitions = []

    # Start at Arad
    current_node = Node.get_node_by_value("Arad", nodes)

    # Steps
    while(not(objective_function(current_node, nodes))):
        new_transition = step_function(current_node, learned_transitions, transitions)
        walked_transitions.append(new_transition)
        current_node = new_transition.to
        current_node.already_walked = new_transition.weight - current_node.heuristic
        print("\n")
        Transition.print_transitions_array(walked_transitions)

main()