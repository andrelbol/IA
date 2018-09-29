import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from plotData import prepare_scatter
from cost import cost, hypothesis
from gradient import gradient

ITERATIONS = 100
ALPHA = 0.8
LAMBDA = 0.8

def main():
  data = pd.read_csv('data/ex2data2.csv')
  initial_X = np.array(data.iloc[:,[0, 1]])
  y = np.array(data.iloc[:,2])
  X = normalize(initial_X)
  mapped_X = np.array([ [1.0, x[0], x[1], x[0]*x[1], x[0]**2, x[1]**2, x[0]*x[1]**2, x[1]*x[0]**2] for x in X ])

  costs = []
  m, n = mapped_X.shape
  theta = np.zeros((n, 1))

  for i in range(0, ITERATIONS):
      costs.append(cost(theta, mapped_X, y, LAMBDA))
      theta = gradient(theta, mapped_X, y, ALPHA, LAMBDA)

  # Testing train data
  hits = 0
  errors = 0
  for i in range(len(X)):
    y_try = 1 if hypothesis(theta, mapped_X[i]) >= 0.5 else 0
    if(y_try == y[i]):
      hits += 1
    else:
      errors += 1

  print("Acertos: {0}".format(hits))
  print("Erros: {0}".format(errors))
  print("Total: {0}".format(hits+errors))
  print("Acurácia: {0}%".format(hits/(hits+errors) * 100))

  # prepare_scatter(X, y)
  plt.show()

def normalize(X):
  return (X-X.min())/(X.max()-X.min())


if __name__ == '__main__':
  main()