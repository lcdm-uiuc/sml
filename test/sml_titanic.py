import sml
from sml import execute

query = 'READ "data/train.csv" (separator = ",", header = 0) AND\
REPLACE (missing="NaN", strategy = "mode") AND SPLIT (train = .8, test = 0.2) AND\
CLASSIFY (predictors = [1,3,4,5,6,7,8,9,10,11,12], label = 2, algorithm = forest)'

def test():
    return execute(query, verbose=None)
if __name__ == '__main__':
    print(test())
