class FuzzyOutput:
  def __init__(self):
    self.parametrics = {}
    self.values = []

  def set_values(self, values):
    self.values = values

  def set_linear_parametric(self, name, a, b):
    self.parametrics[name] = lambda x: a*x + b
  
  def set_sigmoidal_parametric(self, name, a, b):
    self.parametrics[name] = lambda x: a/(b+np.exp(-x))