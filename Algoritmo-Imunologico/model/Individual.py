import random
import numpy as np

mutation_rate = 0.01

class Individual:

  def __init__(self, values):
    self.values = values
    self.fitness = 0

  def clone(self, quantity):
    return [self for i in range(0, quantity)]

  def mutate(self):
    b = random.gauss(0, 1)
    if(random.gauss(-1,1) < mutation_rate):
      for i in range(0, self.values.size):
        self.values[i] += self.values[i]*b*0.05
    return self

  def set_fitness(self, fitness):
    self.fitness = fitness

  def get_fitness(self):
    return self.fitness

  def __str__(self):
    return "Implementar"
