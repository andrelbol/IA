import math
import numpy as np
from model.Individual import Individual

def objective_function(*args):
  x1 = args[0]
  x2 = args[1]
  return -(x2+47)*math.sin(math.sqrt(math.abs(x2+(x1/2)+47))) - x1*math.sin(math.sqrt(math.abs(x1-(x2+47))));

def select_one_chromossome_index(population, total_sum):
  random_number = random.uniform(0, total_sum)
  fitness_sum = 0
  for i in range(0, population.shape[0]):
    fitness_sum += population[i].fitness
    if(fitness_sum >= random_number):
      return i

def initialize():
  int_matrix = np.random.randint(600,size=(100,2))
  population = np.ndarray(shape=(100, 2), dtype=Individual)
  for i in range(0, population.shape[0]):
    population[i] = Individual(int_matrix[i])
  return population

def stop_condition(iter):
  if iter > max_iter:
    return 0;
  return 1;

def eval(P):
  aff_vec = []
  i=0
  for pi in P:
    aff_vec[aff].append(objective_function(pi))
    aff_vec[index].i
    i=i+1
  return aff_vec


def select(population):
  # Calculating objetctive function results
  total_sum = 0
  for i in range(0, population.shape[0]):
    fitness = objective_function(*population[i].values)
    population[i].fitness = fitness
    total_sum += fitness

  new_population = np.ndarray(shape=(population.shape[0], population.shape[1]), dtype=Individual)
  for i in range(0, population.shape[0]):
    index = select_one_chromossome_index(population, total_sum)
    new_population[i] = population[index]

  population =  new_population

def clone(P1, f):
  pass

def mutate(P1, f):
  pass

def replace(P, n2):
  pass

def main():
  population = initialize()
  select(population)
  for i in range(0, population.shape[0]):
    for j in range(0, population.shape[1]):
      print(population[i][j].values)

main()
