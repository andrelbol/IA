import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

class Regression():

  def __init__(self, file_path, alpha):
    data = pd.read_csv(file_path)
    self.x = data.iloc[:, 0]
    self.y = data.iloc[:, 1]
    self.classification = data.iloc[:, 2]
    self.m = len(self.x)
    self.alpha = alpha
    self.theta = np.zeros((2, 1))

  def sigmoid(self, value):
    return 1/(1 + np.exp(-value))

  def hypothesis(self, x):
      z = self.theta[0] + self.theta[1]*x
      return self.sigmoid(z)

  def cost(self):
    accumulator = 0
    for x, y in zip(self.x, self.y):
      h = self.hypothesis(x)
      accumulator -= y*math.log(h)
      accumulator = (1 - y)*math.log(1 - h)
    return (1/self.m)*accumulator


  def gradient_descent(self):
    for j in range(0, len(self.theta)):
      accumulator = 0
      for x, y in zip(self.x, self.y):
        h = self.hypothesis(x)
        print(h)
        accumulator += (h - y) if (j == 0) else (h - y)*x
      self.theta[j] = self.theta[j] - self.alpha*(1/self.m)*accumulator

  def final_function(self, x):
    return self.theta[0] + self.theta[1]*x
