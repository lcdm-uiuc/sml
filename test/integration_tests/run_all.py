import unittest
import sys
import traceback
from sml import execute

class SmlIntegrationTests(unittest.TestCase):

    def test_auto(self):
        query = 'READ "../data/seeds.csv" (separator = "\s+", header = 0) AND SPLIT (train = .8, test = .2, validation = .0) and REPLACE (missing="NaN", strategy="mode") AND CLUSTER (predictors = [1,2,3,4,5,6,7], label = 8, algorithm = kmeans)'
        assert execute(query, verbose=None) is not None

    def test_boston(self):
        query = 'READ "../data/boston.csv" (separator = "\s+", header = 0) AND SPLIT (train = .8, test = .2, validation = .0) AND REGRESS (predictors = [1,2,3,4,5,6,7,8,9,10,11,12,13], label = 14, algorithm = elastic)'
        assert execute(query, verbose=None) is not None

    def test_census(self):
        query = 'READ "../data/census.csv" (separator=",", header = 0, types = [1:numeric, 2:string]) AND REPLACE (missing = "NaN", strategy = "mode") and SPLIT (train = .8, test = 0.2) and CLASSIFY (predictors=[1,2,3,4,5 , 6,7, 8, 9, 10 ,11 ,12, 13,14], label = 15, algorithm = logistic)'
        assert execute(query, verbose=None) is not None

    def test_chronic(self):
        query = 'READ "../data/chronic.csv" (separator = ",", header = None) AND\
        REPLACE (missing="?", strategy = "mode") AND SPLIT (train = .8, test = 0.2) AND CLASSIFY \
        (predictors = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],\
         label = 25, algorithm = logistic)'
        assert execute(query, verbose=None) is not None

    def test_computer(self):
        query = 'READ "../data/computer.csv" (separator = ",", header = 0) AND \
        SPLIT (train = .8, test = .2, validation = .0) AND \
        REGRESS (predictors = [1,2,3,4,5,6,7,8,9], label = 10, algorithm = ridge)'
        assert execute(query, verbose=None) is not None

    def test_iris(self):
        query = 'READ "../data/iris.csv" AND \
         SPLIT (train = .8, test = 0.2) AND \
         CLASSIFY (predictors = [1,2,3,4], label = 5, algorithm = svm)'
        assert execute(query, verbose=None) is not None

    def test_seeds(self):
        query = 'READ "../data/seeds.csv" (separator = "\s+", header = 0) AND SPLIT (train = .8, test = .2, validation = .0) and REPLACE (missing="NaN", strategy="mode") AND CLUSTER (predictors = [1,2,3,4,5,6,7], label = 8, algorithm = kmeans)'
        assert execute(query, verbose=None) is not None

    def test_spam(self):
        query = 'READ "../data/spam.csv" AND SPLIT (train = .8, test = 0.2) AND CLASSIFY (predictors = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56], label = 58, algorithm = bayes)'
        assert execute(query, verbose=None) is not None

    def test_titanic(self):
        query = 'READ "../data/train.csv" (separator = ",", header = 0) AND\
        REPLACE (missing="NaN", strategy="mode") AND SPLIT (train = .8, test = 0.2) AND\
        CLASSIFY (predictors = [1,3,4,5,6,7,8,9,10,11,12], label = 2, algorithm = forest)'
        assert execute(query, verbose=None) is not None

    def test_wine(self):
        query = 'READ "../data/wine.csv" (separator = ";", header = 0) AND SPLIT (train = .8, test = 0.2) AND CLASSIFY (predictors = [1,2,3,4,5,6,7,8,9,10,11], label = 12, algorithm = knn)'
        assert execute(query, verbose=None) is not None

if __name__ == '__main__':
    unittest.main()
