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

def setup_initial_transitions(nodes):
    transitions = []

    transitions.append(Transition(Node.get_node_by_value("Arad", nodes), Node.get_node_by_value("Zerind", nodes), 75))
    transitions.append(Transition(Node.get_node_by_value("Arad", nodes), Node.get_node_by_value("Timisoara", nodes), 118))
    transitions.append(Transition(Node.get_node_by_value("Arad", nodes), Node.get_node_by_value("Sibiu", nodes), 140))
    transitions.append(Transition(Node.get_node_by_value("Zerind", nodes), Node.get_node_by_value("Arad", nodes), 75))
    transitions.append(Transition(Node.get_node_by_value("Zerind", nodes), Node.get_node_by_value("Oradea", nodes), 71))
    transitions.append(Transition(Node.get_node_by_value("Sibiu", nodes), Node.get_node_by_value("Rimnicu Vilcea", nodes), 80))
    transitions.append(Transition(Node.get_node_by_value("Sibiu", nodes), Node.get_node_by_value("Fagaras", nodes), 99))
    transitions.append(Transition(Node.get_node_by_value("Sibiu", nodes), Node.get_node_by_value("Oradea", nodes), 151))
    transitions.append(Transition(Node.get_node_by_value("Sibiu", nodes), Node.get_node_by_value("Arad", nodes), 140))
    transitions.append(Transition(Node.get_node_by_value("Timisoara", nodes), Node.get_node_by_value("Arad", nodes), 118))
    transitions.append(Transition(Node.get_node_by_value("Oradea", nodes), Node.get_node_by_value("Zerind", nodes), 75))
    transitions.append(Transition(Node.get_node_by_value("Oradea", nodes), Node.get_node_by_value("Sibiu", nodes), 151))
    transitions.append(Transition(Node.get_node_by_value("Fagaras", nodes), Node.get_node_by_value("Bucharest", nodes), 211))
    transitions.append(Transition(Node.get_node_by_value("Fagaras", nodes), Node.get_node_by_value("Sibiu", nodes), 99))
    transitions.append(Transition(Node.get_node_by_value("Rimnicu Vilcea", nodes), Node.get_node_by_value("Pitesi", nodes), 97))
    transitions.append(Transition(Node.get_node_by_value("Rimnicu Vilcea", nodes), Node.get_node_by_value("Sibiu", nodes), 80))
    transitions.append(Transition(Node.get_node_by_value("Rimnicu Vilcea", nodes), Node.get_node_by_value("Craiova", nodes), 146))
    transitions.append(Transition(Node.get_node_by_value("Pitesi", nodes), Node.get_node_by_value("Bucharest", nodes), 101))
    transitions.append(Transition(Node.get_node_by_value("Pitesi", nodes), Node.get_node_by_value("Rimnicu Vilcea", nodes), 97))
    transitions.append(Transition(Node.get_node_by_value("Pitesi", nodes), Node.get_node_by_value("Craiova", nodes), 138))
    transitions.append(Transition(Node.get_node_by_value("Craiova", nodes), Node.get_node_by_value("Rimnicu Vilcea", nodes), 145))
    transitions.append(Transition(Node.get_node_by_value("Craiova", nodes), Node.get_node_by_value("Pitesi", nodes), 138))
    return transitions
