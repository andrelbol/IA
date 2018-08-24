import os, sys
sys.path.append('{0}/../models'.format(os.getcwd()))

import numpy as np
from random import shuffle
import matplotlib.pyplot as plt
from FuzzyInput import FuzzyInput
from FuzzyOutput import FuzzyOutput


PARTITION_START = -2
PARTITION_END = 2
NUMBER_OF_POINTS = 20
EPOCHS = 400
ALPHA = 0.1

objective_function = lambda x: x**2

x = FuzzyInput(list(np.linspace(PARTITION_START, PARTITION_END, NUMBER_OF_POINTS)))
y = [objective_function(i) for i in x.values]

a1, b1, a2, b2 = 1, 1, -1, 1
x.set_sigmoidal_partition('Sig1', a1, b1)
x.set_sigmoidal_partition('Sig2', a2, b2)

output = FuzzyOutput()
p1, r1, p2, r2 = -0.1, -0.2, 0.1, 0.3
output.set_linear_parametric("Lin1", p1, r1)
output.set_linear_parametric("Lin2", p2, r2)

def weighted_average(value):
  num, den = 0, 0
  for partition, parametric in zip(x.partitions, output.parametrics):
    num += x.partitions[partition](value)*output.parametrics[parametric](value)
    den += x.partitions[partition](value)
  return num/den

deriv_a1 = lambda value: x.partitions['Sig2'](value) * ((output.parametrics['Lin1'](value) -
  output.parametrics['Lin2'](value))/np.power((x.partitions['Sig1'](value) + x.partitions['Sig2'](value)),2)) * x.partitions['Sig1'](value) * ((value-a1)/np.power(b1,2))
deriv_a2 = lambda value: x.partitions['Sig1'](value) * ((output.parametrics['Lin2'](value) -
  output.parametrics['Lin1'](value))/np.power((x.partitions['Sig1'](value) + x.partitions['Sig2'](value)),2)) * x.partitions['Sig2'](value) * ((value-a2)/np.power(b2,2))
deriv_b1 = lambda value: x.partitions['Sig2'](value) * ((output.parametrics['Lin1'](value) -
  output.parametrics['Lin2'](value))/np.power((x.partitions['Sig1'](value) + x.partitions['Sig2'](value)),2)) * x.partitions['Sig1'](value) * (np.power((value-a1),2)/np.power(b1,3))
deriv_b2 = lambda value: x.partitions['Sig1'](value) * ((output.parametrics['Lin2'](value) -
  output.parametrics['Lin1'](value))/np.power((x.partitions['Sig1'](value) + x.partitions['Sig2'](value)),2)) * x.partitions['Sig2'](value) * (np.power((value-a1),2)/np.power(b2,3))
deriv_p1 = lambda value: x.partitions['Sig1'](value)*value/(x.partitions['Sig1'](value)+x.partitions['Sig2'](value))
deriv_p2 = lambda value: x.partitions['Sig2'](value)*value/(x.partitions['Sig1'](value)+x.partitions['Sig2'](value))
deriv_r1 = lambda value: x.partitions['Sig1'](value)/(x.partitions['Sig1'](value)+x.partitions['Sig2'](value))
deriv_r2 = lambda value: x.partitions['Sig2'](value)/(x.partitions['Sig1'](value)+x.partitions['Sig2'](value))

index_array = list(range(NUMBER_OF_POINTS))

epoch = 0
errors = []
while epoch < EPOCHS:
  shuffle(index_array)
  total_error = 0
  for index in index_array:
    y_pred = weighted_average(x.values[index])
    error = y[index] - y_pred

    total_error += error
    a1 = a1 + (error*ALPHA*deriv_a1(x.values[index]))
    a2 = a2 + (error*ALPHA*deriv_a2(x.values[index]))
    b1 = b1 + (error*ALPHA*deriv_b1(x.values[index]))
    b2 = b2 + (error*ALPHA*deriv_b2(x.values[index]))
    p1 = p1 + (error*ALPHA*deriv_p1(x.values[index]))
    p2 = p2 + (error*ALPHA*deriv_p2(x.values[index]))
    r1 = r1 + (error*ALPHA*deriv_r1(x.values[index]))
    r2 = r2 + (error*ALPHA*deriv_r2(x.values[index]))
    
    x.set_sigmoidal_partition('Sig1', a1, b1)
    x.set_sigmoidal_partition('Sig2', a2, b2)
    output.set_linear_parametric("Lin1", p1, r1)
    output.set_linear_parametric("Lin2", p2, r2)

  errors.append(total_error)
  epoch += 1


y_pred = [weighted_average(i) for i in x.values]

plt.plot(x.values, y,x.values, y_pred)
plt.show()
plt.plot(errors)