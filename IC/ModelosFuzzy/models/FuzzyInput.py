import numpy as np

class FuzzyInput:
  
  def __init__(self, values):
    self.values = values
    self.partitions = {}

  def set_linear_partition(self, name, a, b):
    self.partitions[name] = lambda x: a*x + b
  
  def set_sigmoidal_partition(self, name, a, b):
    self.partitions[name] = lambda x: np.exp(-0.5*np.power((x-a)/(b), 2))
    # self.partitions[name] = lambda x: a/(b+np.exp(-x))