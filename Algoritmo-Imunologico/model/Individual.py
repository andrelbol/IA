import numpy as np

class Individual:

  def __init__(self):
    self.fitness = 0
    pass

  def clone(self, quantity):
    return [self for i in range(0, quantity)]

  def mutate(self):
    pass

  def set_fitness(self, fitness):
    self.fitness = fitness

  def get_fitness(self):
    return self.fitness

  def __str__(self):
    return "Implementar"