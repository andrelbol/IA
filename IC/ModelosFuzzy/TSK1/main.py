import os, sys
sys.path.append('{0}/../models'.format(os.getcwd()))

import numpy as np
from numpy.linalg import pinv
from random import shuffle
import matplotlib.pyplot as plt
from FuzzyInput import FuzzyInput
from FuzzyOutput import FuzzyOutput

inputx = FuzzyInput([-0.91, -0.77, -0.44, -0.39, -0.21 , -0.01 , 0.22 , 0.33 , 0.47, 0.65, 0.85, 0.89])
y = np.array([0.9101,  0.6469,  0.1816,  0.1301, -0.0139, -0.0979, -0.0956, -0.0571,  0.0269,  0.1925,  0.4525,  0.5141])

a1, b1, a2, b2 = -0.8, 0.4, 0.8, 0.4
inputx.set_linear_partition('Lin1', a1, b1)
inputx.set_linear_partition('Lin2', a2, b2)

beta_calc_1 = lambda value: inputx.partitions['Lin1'](value)/(inputx.partitions['Lin1'](value) + inputx.partitions['Lin2'](value))
beta_calc_2 = lambda value: inputx.partitions['Lin2'](value)/(inputx.partitions['Lin1'](value) + inputx.partitions['Lin2'](value))
beta_calc_3 = lambda value: inputx.partitions['Lin1'](value)*value/(inputx.partitions['Lin1'](value) + inputx.partitions['Lin2'](value))
beta_calc_4 = lambda value: inputx.partitions['Lin2'](value)*value/(inputx.partitions['Lin1'](value) + inputx.partitions['Lin2'](value))

beta = []
beta.append([beta_calc_1(i) for i in inputx.values])
beta.append([beta_calc_2(i) for i in inputx.values])
beta.append([beta_calc_3(i) for i in inputx.values])
beta.append([beta_calc_4(i) for i in inputx.values])


inv_beta = pinv(np.array(beta))
final_matrix = np.matmul(inv_beta.T, y)
r1, r2, p1, p2  = final_matrix

outputy = FuzzyOutput()
outputy.set_linear_parametric("Lin1", p1, r1)
outputy.set_linear_parametric("Lin2", p2, r2)

def weighted_average(value):
  num, den = 0, 0
  for partition, parametric in zip(inputx.partitions, outputy.parametrics):
    num += inputx.partitions[partition](value)*outputy.parametrics[parametric](value)
    den += inputx.partitions[partition](value)
  return num/den

y_pred = [weighted_average(i) for i in inputx.values]

plt.plot(inputx.values, y_pred)
plt.show()