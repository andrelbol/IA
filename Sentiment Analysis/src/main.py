import re

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def main():
  # Reading data from file
  reviews_train = process_file_content(read_data("train"))
  reviews_test = process_file_content(read_data("test"))
  
  # Building vectors from files to treat them
  train_vector = vectorize(reviews_train)
  test_vector = vectorize(reviews_test)

  # Preparing data for training
  target = [1 if i < 12500 else 0 for i in range(25000)]
  X_train, X_val, y_train, y_val = train_test_split(
      train_vector, target, train_size = 0.75
  )

  # Training with multiple values of regularization factor
  for c in [0.01, 0.05, 0.25, 0.5, 1]:
    lr = LogisticRegression(C=c)
    lr.fit(X_train, y_train)
    print ("Accuracy for C={0}: {1}".format(c, accuracy_score(y_val, lr.predict(X_val))))
    
  # Building the final model with the best regularization factor
  final_model = LogisticRegression(C=0.05)
  final_model.fit(train_vector, target)

  # Getting the 5 best positive words 
  get_best_results(reviews_train, final_model)

  # Getting the 5 best negative words
  get_best_results(reviews_train, final_model, False)

def read_data(set_type):
  """ Read data from a txt file. The set_type can be 'train' or 'test'. """
  reviews = []
  for line in open('../data/aclImdb/movie_data/full_{0}.txt'.format(set_type), 'r'):
    reviews.append(line.strip())
  
  return reviews
  
def process_file_content(content):
  """ Convert the content of the txt file into a formatted content. """
  no_space_regex = re.compile("(\.)|(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\()|(\))|(\[)|(\])")
  with_space_regex = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")

  reviews = [no_space_regex.sub("", line.lower()) for line in content]
  reviews = [with_space_regex.sub(" ", line) for line in reviews]
    
  return reviews

def vectorize(dataset):
  """ Convert the content data into vectors that can be analyzed. """
  countVectorizer = CountVectorizer(binary=True)
  countVectorizer.fit(dataset)
  return countVectorizer.transform(dataset)

def get_best_results(dataset, model, positive=True, quantity=5):
  countVectorizer = CountVectorizer(binary=True)
  countVectorizer.fit(dataset)
  bests = []

  feature_to_coef = {
    word: coef for word, coef in zip(
        countVectorizer.get_feature_names(), model.coef_[0]
    )
  }
  sorted_words = sorted(
    feature_to_coef.items(), 
    key=lambda x: x[1], 
    reverse=positive)

  for best in sorted_words[:5]:
    bests.append(best)
    print (best)
  return bests

if __name__ == "__main__":
  main()