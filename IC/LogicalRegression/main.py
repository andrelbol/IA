import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from plotData import prepare_scatter
from cost import cost
from gradient import gradient

ITERATIONS = 100
ALPHA = 0.8

def main():
    data = pd.read_csv('data/ex2data1.csv')
    initial_X = np.array(data.iloc[:,[0, 1]])
    y = np.array(data.iloc[:,2])
    X = normalize(initial_X)

    # Concatenate column of ones
    m, n = X.shape
    ones = np.array([np.ones(m)])
    concat_X = np.concatenate((ones.T, X), axis=1)

    costs = []
    theta = np.zeros((n+1, 1))

    for i in range(0, ITERATIONS):
        costs.append(cost(theta, concat_X, y))
        theta = gradient(theta, concat_X, y, ALPHA)


    prepare_scatter(X, y)

    print(theta)

    final_func = lambda x: (-theta[1]*x - theta[0])/theta[2]
    x_axis_values = [ i/1000 for i in range(0, 1000) ]
    y_axis_values = [ final_func(x) for x in x_axis_values]
    plt.plot(x_axis_values, y_axis_values, 'r--')
    plt.show()

def normalize(X):
    return (X-X.min())/(X.max()-X.min())

if __name__ == '__main__':
    main()
