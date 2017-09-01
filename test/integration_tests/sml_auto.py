import sml
from sml import execute

query = 'READ "../data/auto.csv" (separator = "\s+", header = None) AND\
 REPLACE (missing = "?", strategy = "mode") AND\
  SPLIT (train = .8, test = .2) AND \
  REGRESS (predictors = [2,3,4,5,6,7,8], label = 1, algorithm = lasso)'

def test():
    return execute(query, verbose=None)

if __name__ == '__main__':
    print(test())
