import math, random
import numpy as np
from functools import reduce

import matplotlib.pyplot as plt

POPULATION_SIZE = 100
MUTATION_RATE = 0.01
GENERATIONS = 500

# Funções Utilitárias
reduce_sum_func = lambda prev,curr: prev + curr
reduce_objective_sum_func = lambda prev,curr: prev + objective_function(*curr)

# Função Objetivo
def objective_function(*args):
    x1 = args[0]
    x2 = args[1]
    func = -(x2 + 47)*math.sin(math.sqrt(abs(x2 + x1/2 + 47))) - x1*math.sin(math.sqrt(abs(x1 - (x2 + 47))))
    return -1*func + 1500

class GeneticAlgorithm:

  def __init__(self):
    self.population = np.random.randint(600,size=(POPULATION_SIZE,2))
    self.population_fitness = []
    self.best_array = []
    self.medium_array = []

  def evaluate(self):
    fitness_array = [ objective_function(*individual) for individual in self.population ]
    self.population_fitness = sorted(fitness_array, reverse=True)

  def roulette(self):
    index = 0
    fitness_sum = 0
    total_fitness = reduce(reduce_sum_func, self.population_fitness)
    while(fitness_sum < random.uniform(0, total_fitness)):
      fitness_sum += self.population_fitness[index]
      index += 1 
    return (index-1)

  def select(self):
    self.evaluate()
    selected_population = [ self.population[self.roulette()] for i in self.population ]
    self.population = selected_population

  def crossover(self):
    crossed_population = np.zeros([POPULATION_SIZE, 2])
    population_half = math.floor(POPULATION_SIZE/2)
    alpha = random.uniform(0.25, 1.25)
    cross = lambda x,y: alpha*x + (1 - alpha)*y
    for i in range(0, population_half):
      first = self.population[i]
      second = self.population[i+population_half]
      for j in range(0, 2):
        crossed_population[i][j] = cross(first[j], second[j])
        crossed_population[i+population_half][j] = cross(second[j], first[j])
    self.population = crossed_population

  def mutate(self):
    self.population = [ self.__mutate(individual) for individual in self.population ]

  def __mutate(self, individual):
    b = random.gauss(-1, 1)
    increment = lambda x: x + x*b*0.02
    if(random.gauss(0,1) < MUTATION_RATE):
      mutated_individual = [ increment(x) for x in individual ]
      return mutated_individual
    return list(individual)
    
  def plot_results(self):
    t = range(0, len(self.best_array))
    desired = [ objective_function(512, 404.2319) for i in t]
    plt.plot(t, self.best_array, 'r--', t, self.medium_array, 'b--', t, desired, 'g--')
    plt.show()

  def run(self):
    for i in range(0, GENERATIONS):
      self.select()
      self.crossover()
      self.mutate()
      self.best_array.append(objective_function(*self.population[0]))
      self.medium_array.append(reduce(reduce_objective_sum_func, self.population)/POPULATION_SIZE)

ga = GeneticAlgorithm()
ga.run()
ga.plot_results()