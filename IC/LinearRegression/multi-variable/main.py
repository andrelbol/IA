import matplotlib.pyplot as plt

from models.Regression import Regression

def main():
  file_path = '../data/ex2data1.csv'
  regression = Regression(file_path, 0.01)
  plt.figure(1)
  plt.xlabel('Exam1 score')
  plt.ylabel('Exam1 score')
  plt.scatter(regression.x, regression.y)
  costs = []
  for i in range(0, 2000):
    regression.gradient_descent()
    costs.append(regression.cost())

  y = [regression.final_function(x) for x in regression.x]
  plt.plot(regression.x, y, 'r--')
  plt.figure(2)
  plt.ylabel('Função custo')
  plt.xlabel('Index')
  plt.plot(range(0, len(costs)), costs, 'r--')
  plt.show()

if __name__ == '__main__':
  main()
