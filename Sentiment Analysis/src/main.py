import re

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def main():
  reviews_train = process_file_content(read_data("train"))
  reviews_test = process_file_content(read_data("test"))
  # TODO: continuar

def read_data(set_type="train"):
  reviews = []
  for line in open('../data/aclImdb/movie_data/full_{0}.txt'.format(set_type), 'r'):
    reviews.append(line.strip())
  
  return reviews
  
def process_file_content(content):
  no_space_regex = re.compile("(\.)|(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\()|(\))|(\[)|(\])")
  with_space_regex = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")

  reviews = [no_space_regex.sub("", line.lower()) for line in content]
  reviews = [with_space_regex.sub(" ", line) for line in reviews]
    
  return reviews

def vectorize(dataset):
  countVectorizer = CountVectorizer(binary=True)
  countVectorizer.fit(dataset)
  return countVectorizer.transform(dataset)

if __name__ == "__main__":
  main()