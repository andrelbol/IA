import numpy as np

"""
  Entradas encontradas no problema
"""
x = np.array([-0.91, -0.77, -0.44, -0.39, -0.21 , -0.01 , 0.22 , 0.33 , 0.47, 0.65, 0.85, 0.89])
y = np.array([0.9101,  0.6469,  0.1816,  0.1301, -0.0139, -0.0979, -0.0956, -0.0571,  0.0269,  0.1925,  0.4525,  0.5141])

"""
  As partições definidas são:
  1 - Favorece valores negativos
  2 - Favorece valores positivos
"""
neg_partition = np.array([(-i + 0.89)/1.8 for i in x])
pos_partition = np.array([(i + 0.91)/1.8 for i in x])

"""
  As regras são 2:
  1 - Se o valor é negativo, sua função é -2 * x
  2 - Se o valor é positivo, sua função é 2 * x
"""
def rule_function_one(value):
  return -2 * value;

def rule_function_two(value):
  return 2 * value;