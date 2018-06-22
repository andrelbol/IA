import numpy as np
import math, random
from functools import reduce

import matplotlib.pyplot as plt

# Restrições
MAX_ITERATIONS = 50;
POPULATION_SIZE = 100;
SELECTION_SIZE = 50;
CLONE_RATE = 5; 
MUTATION_INCREMENT = 0.2;
MUTATION_RATE = 0.2;
COORDS_MIN = -600
COORDS_MAX = 600

# Funções utilitárias
# Se estiver no limite, joga pro meio de novo (COORDS_MAX/2 é só um valor médio pra modificar)
limit_max = lambda x: x if x < COORDS_MAX else x - COORDS_MAX/2
limit_min = lambda x: x if x > COORDS_MIN else x + COORDS_MAX/2
reduce_sum_func = lambda prev,curr: prev + objective_function(*curr)

# Função Objetivo
def objective_function(*args):
    x1 = args[0]
    x2 = args[1]
    func = -(x2 + 47)*math.sin(math.sqrt(abs(x2 + x1/2 + 47))) - x1*math.sin(math.sqrt(abs(x1 - (x2 + 47))))
    return -1*func + 1500

class ImunologicAlgorithm:
  
  def __init__(self):
    self.population = np.random.randint(600,size=(POPULATION_SIZE,2))
    self.best_array = []
    self.medium_array = []

  def select(self):
    # Sort by affinity
    reverse_sorted_population = sorted(
      self.population, 
      key=lambda individual: objective_function(*individual),
      reverse=True
    )
    self.population = reverse_sorted_population[:SELECTION_SIZE]

  def clone(self):
    cloned_population = []
    for individual in self.population:
      cloned_population.extend([individual for i in range(0, CLONE_RATE)]) 
    self.population = cloned_population

  def mutate(self):
    mutated_population = []
    for individual in self.population:
      mutated_population.append(self.__mutate(individual))
    self.population =  mutated_population

  def __mutate(self, individual):
    b = random.gauss(-1, 1)
    increment = lambda x: x + x*b*MUTATION_INCREMENT
    if(random.gauss(0,1) < MUTATION_RATE):
      mutated_individual = [ increment(x) for x in individual]
      mutated_individual = [ limit_max(x) for x in mutated_individual ]
      mutated_individual = [ limit_min(x) for x in mutated_individual ]
      return mutated_individual
    return list(individual)

  def plot_results(self):
    t = range(0, len(self.best_array))
    desired = [ objective_function(512, 404.2319) for i in t]
    plt.plot(t, self.best_array, 'r--', t, self.medium_array, 'b--', t, desired, 'g--')
    plt.show()

  def run(self):
    best_array = []
    medium_array = []
    for t in range(0, MAX_ITERATIONS):
      self.select()
      self.clone()
      self.mutate()
      self.select()
      self.best_array.append(objective_function(*self.population[0]))
      self.medium_array.append(reduce(reduce_sum_func, self.population)/SELECTION_SIZE)

# Execução
ia = ImunologicAlgorithm()
ia.run()
ia.plot_results()
