class Transition:

    def __init__(self, current, to, weight):
        self.current = current
        self.to = to
        self.weight = weight

    @staticmethod
    def get_shortest_transition(transitions):
        best_transition = transitions[0]
        for transition in transitions:
            if(best_transition.weight > transition.weight):
                best_transition = transition
        return best_transition

    @staticmethod
    def remove_walked_path(transitions, walked_path):
        # Remove the walked transition, and the inverse of it (you can't go back in a search)
        aux_list = list(transitions) # Need to make a copy because will change the original
        for transition in aux_list:
            if((transition.to == walked_path.to and transition.current == walked_path.current)
                or (transition.to == walked_path.current and transition.current == walked_path.to)):
                transitions.remove(transition)

    @staticmethod
    def print_transitions_array(transitions):
        for transition in transitions:
            print(transition)

    def __str__(self):
        FROM = self.current.value
        TO = self.to.value
        F_VAL = str(self.weight)
        G_VAL = str(self.weight - self.to.heuristic)
        H_VAL = str(self.to.heuristic)
        return "From: " + FROM + ", To: " + TO + ", f: " + F_VAL + ", g: " + G_VAL + ", h: " + H_VAL
