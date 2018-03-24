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

    def __str__(self):
        return self.value