import matplotlib.pyplot as plt

def prepare_scatter(X, Y):
  pos, neg = X[Y == 1], X[Y == 0]
  plt.scatter(pos[:, 0], pos[:, 1], c='y')
  plt.scatter(neg[:, 0], neg[:, 1], c='b')
  plt.xlabel('Exam 1 score')
  plt.ylabel('Exam 2 score')
