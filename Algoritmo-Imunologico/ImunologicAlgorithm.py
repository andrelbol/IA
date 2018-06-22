import numpy as np
import math, random
from functools import reduce

import matplotlib.pyplot as plt

# Restrições
max_iterations = 50;
population_size = 100;
selection_size = 50;
clone_rate = 5; 
mutation_increment = 0.2;
mutation_rate = 0.2;

# Função Objetivo
def objective_function(*args):
    x1 = args[0]
    x2 = args[1]
    func = -(x2 + 47)*math.sin(math.sqrt(abs(x2 + x1/2 + 47))) - x1*math.sin(math.sqrt(abs(x1 - (x2 + 47))))
    return -1*func + 1500

class ImunologicAlgorithm:
  
  def __init__(self):
    self.population = np.random.randint(600,size=(population_size,2))
    self.population_fitness = []
    self.best_array = []
    self.medium_array = []

  def evaluate(self):
    fitness_array = []
    for individual in self.population:
      fitness_array.append(objective_function(individual))
    self.population_fitness = fitness_array

  def select(self):
    # Sort by affinity
    reverse_sorted_population = sorted(
      self.population, 
      key=lambda individual: objective_function(*individual),
      reverse=True
    )
    self.population = reverse_sorted_population[:selection_size]

  def clone(self):
    cloned_population = []
    for individual in self.population:
      cloned_population.extend([individual for i in range(0, clone_rate)]) 
    self.population = cloned_population

  def mutate(self):
    mutated_population = []
    for individual in self.population:
      mutated_population.append(self.__mutate(individual))
    self.population =  mutated_population

  def __mutate(self, individual):
    b = random.gauss(-1, 1)
    if(random.gauss(0,1) < mutation_rate):
      return [ (x + x*b*0.5) for x in individual]
    else:
      return list(individual)

  def plot_results(self):
    t = range(0, len(self.best_array))
    plt.plot(t, self.best_array, 'r--', t, self.medium_array, 'b--')
    plt.show()

  def run(self):
    best_array = []
    medium_array = []
    reduce_sum_func = lambda prev,curr: prev + objective_function(*curr)
    for t in range(0, max_iterations):
      self.select()
      self.clone()
      self.mutate()
      self.select()
      self.best_array.append(objective_function(*self.population[0]))
      self.medium_array.append(reduce(reduce_sum_func, self.population)/selection_size)

# Execução
ia = ImunologicAlgorithm()
ia.run()
ia.plot_results()