import sml
from sml import execute

query = 'READ "../data/seeds.csv" (separator = "\s+", header = 0) AND SPLIT (train = .8, test = .2, validation = .0) and REPLACE (missing="NaN", strategy="mode") AND CLUSTER (predictors = [1,2,3,4,5,6,7], label = 8, algorithm = kmeans)'

def test():
    return execute(query, verbose=None)
if __name__ == '__main__':
    print(test())
