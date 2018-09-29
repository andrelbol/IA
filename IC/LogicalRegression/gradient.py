import numpy

from cost import hypothesis

def gradient(theta, X, Y, alpha):
  m, n = X.shape
  for j in range(0, len(theta)):
    derivative = 0
    for x, y in zip(X, Y):
      derivative += (hypothesis(theta, x) - y)*x[j]
    
    theta[j] = theta[j] - (alpha/m) * derivative
  return theta

