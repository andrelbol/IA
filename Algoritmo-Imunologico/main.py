import math
import numpy as np
from model.Individual import Individual

def objective_function(*args):
  x1 = args[0]
  x2 = args[1]
  return -(x2+47)*math.sin(math.sqrt(math.abs(x2+(x1/2)+47))) - x1*math.sin(math.sqrt(math.abs(x1-(x2+47))));

def generate_initial_population():
  pass



def initialize():
  population = np.random.randint(600,size=(100,2))
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


def select(P, n1, f):
  pass

def clone(P1, f):
  pass

def mutate(P1, f):
  pass

def replace(P, n2):
  pass

def main():
  pass
