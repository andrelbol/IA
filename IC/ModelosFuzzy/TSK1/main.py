import numpy as np
from random import shuffle
import matplotlib.pyplot as plt

x = np.array([-0.91, -0.77, -0.44, -0.39, -0.21 , -0.01 , 0.22 , 0.33 , 0.47, 0.65, 0.85, 0.89])
y = np.array([0.9101,  0.6469,  0.1816,  0.1301, -0.0139, -0.0979, -0.0956, -0.0571,  0.0269,  0.1925,  0.4525,  0.5141])

'''
 -- Fuzzy Partitions --
 There is a negative and a positive ones. The relevance is defined by lines (f(x) = ax + b)
 Negative one: f1(x) = a1x + b1
 Positive one: f2(x) = a2x + b2
'''
a1, b1, a2, b2 = -0.8, 0.4, 0.8, 0.4
negative_partition_relevance = lambda x: a1*x + b1
positive_partition_relevance = lambda x: a2*x + b2

'''
  -- Rules Output Functions --
  Similar to the partitions, are lines too (f(x) = cx + d)
  As there are 2 rules, onde for each partition because there's only one input
  Rule1: z1(x) = c1x + d1
  Rule2: z2(x) = c2x + d2
'''
c1, d1, c2, d2 = -0.2, 0.2, 0.3, 0.4
rule1_output = lambda x: c1*x + d1
rule2_output = lambda x: c2*x + d2

'''
  -- Weigth Average --
  Used to calculate the final output of the fuzzy system.
  weigthed_average = (relevance*rule_output)/(sum_relevances)
'''
num = lambda x: negative_partition_relevance(x) * rule1_output(x) + positive_partition_relevance(x) * rule2_output(x)
den = lambda x: negative_partition_relevance(x) + positive_partition_relevance(x)
weigthed_average = lambda x: num(x)/den(x)

'''
  -- Gradient Method --
  Needs to calculate the derivative of the weigthed average for each parameter of functions.
'''
def derivative_first_order_parameter(partition_relevance_function, value):
  return partition_relevance_function(value)*value/den(value)

def derivative_zero_order_parameter(partition_relevance_function, value):
  return partition_relevance_function(value)/den(value)

'''
  -- Training --
  The system must be trained to adapt the parameters os the fuzzy system.
'''
MAX_ITERATIONS = 400
errors = []
for iter in range(0, MAX_ITERATIONS):
  index_array = list(range(0, len(x)))
  shuffle(index_array)
  for index in index_array:
    y_calculated = weigthed_average(x[index])
    error = y[index] - y_calculated
    a1 = a1 + error*0.001*derivative_first_order_parameter(negative_partition_relevance, x[index])
    b1 = b1 + error*0.001*derivative_zero_order_parameter(negative_partition_relevance, x[index])
    a2 = a2 + error*0.001*derivative_first_order_parameter(positive_partition_relevance, x[index])
    b2 = b2 + error*0.001*derivative_zero_order_parameter(positive_partition_relevance, x[index])
    c1 = c1 + error*0.001*derivative_first_order_parameter(negative_partition_relevance, x[index])
    d1 = d1 + error*0.001*derivative_zero_order_parameter(negative_partition_relevance, x[index])
    a2 = c2 + error*0.001*derivative_first_order_parameter(positive_partition_relevance, x[index])
    d2 = d2 + error*0.001*derivative_zero_order_parameter(positive_partition_relevance, x[index])
    errors.append(error)
final_results_array = [weigthed_average(i) for i in x]

# plt.plot(x, y, x, final_results_array)
plt.plot(range(0, len(errors)), errors)
plt.show()


