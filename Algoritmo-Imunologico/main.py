import math
import numpy as np

def objective_function(pi):
  x1 = pi[0]
  x2 = pi[1]
  return -(x2+47)*math.sin(math.sqrt(math.abs(x2+(x1/2)+47))) - x1*math.sin(math.sqrt(math.abs(x1-(x2+47))));

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


def clone(P1, f):


def mutate(P1, f):


def replace(P, n2):