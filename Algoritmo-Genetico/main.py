import math, random
import numpy as np

def objective_function(*args):
  x1 = args[0]
  x2 = args[1]
  func = -(x2 + 47)*math.sin(math.sqrt(abs(x2 + x1/2 + 47))) - x1*math.sin(math.sqrt(abs(x1 - (x2 + 47))))
  return func + 959.6407

def select_one_chrom_index(population_fitness, total_sum):
  random_number = random.uniform(0, total_sum)
  print(random_number)
  fitness_sum = 0
  for i in range(0, population_fitness.shape[0]):
    fitness_sum += population_fitness[i]
    if(fitness_sum >= random_number):
      return i

def generate_population():
  population = np.random.randint(600, size=(100, 2))
  return population 

def select(population):
  population_count = population.shape[0]
  population_size = population.shape[1]
  population_fitness = np.zeros([population_count])
  new_population_count = math.floor(population_count*0.8)
  new_population = np.zeros([new_population_count, population_size])

  total_sum = 0
  for i in range(0, population_count):
    fitness = objective_function(*population[i])
    population_fitness[i] = fitness
    total_sum += fitness

  for i in range(0, new_population_count):
    index = select_one_chrom_index(population_fitness, total_sum)
    new_population[i] = population[index]

  return new_population

# TODO(@andre-luis): Perguntar em qual momento colocar isso
def evaluate(population):
  pass

def crossover(population):
  population_count = population.shape[0]
  population_size = population.shape[1]
  population_half = math.floor(population_count/2)
  new_population = np.zeros([population_count, population_size])
  alpha = random.uniform(0.25, 1.25)
  for i in range(0, population_half):
    first = population[i]
    second = population[i+population_half]
    for j in range(0, population_size):
      new_population[i][j] = alpha*first[j] + (1 - alpha)*second[j]
      new_population[i+population_half][j] = alpha*second[j] + (1 - alpha)*first[j]

  return new_population

# TODO(@andre-luis): Perguntar se realmente é necessário transformar para binário para mutar 
def mutate(population):
  pass

def main():
  population = generate_population()
  crossed_population = crossover(population)
  selected_population = select(crossed_population)
  print(selected_population)
  return
  

main()