import math, random
import numpy as np
import matplotlib.pyplot as plt

class GeneticAlgorithm:

  def __init__(self):
    self.population = self.generate_population()
    self.population_count = self.population.shape[0]
    self.population_size = self.population.shape[1]
    self.mutation_rate = 0.01
    self.number_of_generations = 1000

  def objective_function(self, *args):
    x1 = args[0]
    x2 = args[1]
    func = -(x2 + 47)*math.sin(math.sqrt(abs(x2 + x1/2 + 47))) - x1*math.sin(math.sqrt(abs(x1 - (x2 + 47))))
    return -1*func + 1500

  def get_best_evaluate(self):
    value = 0
    for i in range(0, self.population_count):
      new_value = self.objective_function(*self.population[i])
      if(new_value > value):
        value = new_value
    return value

  def get_generation_medium(self):
    medium = 0
    for i in range(0, self.population_count):
      medium += self.objective_function(*self.population[i])
    medium /= self.population_count
    return medium

  def select_one_chromossome_index(self, population_fitness, total_sum):
    random_number = random.uniform(0, total_sum)
    fitness_sum = 0
    for i in range(0, self.population_count):
      fitness_sum += population_fitness[i]
      if(fitness_sum >= random_number):
        return i

  def generate_population(self):
    population = np.random.randint(600, size=(100, 2))
    return population

  def select(self):
    population_fitness = np.zeros([self.population_count])
    new_population = np.zeros([self.population_count, self.population_size])

    # Calculating objetctive function results
    total_sum = 0
    for i in range(0, self.population_count):
      fitness = self.objective_function(*self.population[i])
      population_fitness[i] = fitness
      total_sum += fitness

    #
    for i in range(0, self.population_count):
      index = self.select_one_chromossome_index(population_fitness, total_sum)
      new_population[i] = self.population[index]

    self.population =  new_population

  def crossover(self):
    population_half = math.floor(self.population_count/2)
    new_population = np.zeros([self.population_count, self.population_size])
    alpha = random.uniform(0.25, 1.25)
    for i in range(0, population_half):
      first = self.population[i]
      second = self.population[i+population_half]
      for j in range(0, self.population_size):
        new_population[i][j] = alpha*first[j] + (1 - alpha)*second[j]
        new_population[i+population_half][j] = alpha*second[j] + (1 - alpha)*first[j]

    self.population = new_population

  def mutate(self):
    b = random.gauss(0, 1)
    for i in range(0, self.population_count):
      if(random.gauss(0, 1) < self.mutation_rate):
        for j in range(0, self.population_size):
          self.population[i][j] += self.population[i][j]*b*0.05


  def run(self):
    best_offspring_array = []
    medium_array = []
    for i in range(0, self.number_of_generations):
      self.select()
      self.crossover()
      self.mutate()
      best_offspring_array.append(self.get_best_evaluate())
      medium_array.append(self.get_generation_medium())
    print(self.population)
    return best_offspring_array, medium_array


ag = GeneticAlgorithm()
value_array, medium_array = ag.run()
desired_array = []
for i in range(0, ag.number_of_generations):
    desired_array.append(1500 + 959.6407)
t = range(0, ag.number_of_generations)
plt.plot(t, value_array, 'r--', t, medium_array, 'b--', t, desired_array, 'g--')
plt.show()