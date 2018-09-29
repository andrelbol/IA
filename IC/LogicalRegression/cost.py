import numpy as np
from math import log

def cost(theta, X, Y):
  m, n = X.shape
  accumulator = 0
  for x, y in zip(X, Y):
    first_param = -y*log(hypothesis(theta, x))
    second_param = (1 - y)*log(1 - hypothesis(theta, x))
    accumulator += first_param - second_param

  return (1/m)*accumulator

def hypothesis(theta, x):
  accumulator = 0
  for pair in zip(theta, x):
    accumulator += pair[0]*pair[1]
  return sigmoid(accumulator)

def sigmoid(z):
  return 1/(1 + np.exp(-z))
