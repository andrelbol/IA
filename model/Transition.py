class Transition:

    def __init__(self, current, to, weight):
        self.current = current
        self.to = to
        self.weight = weight

    def __str__(self):
        return "From: " + self.current.value + ", To: " + self.to.value + ", weight: " + str(self.weight)
