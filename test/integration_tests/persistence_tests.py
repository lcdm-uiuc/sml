import unittest
import sys
import traceback
import os.path
from sml import execute
class sml_integragtion_tests(unittest.TestCase):
    def test_persistence_preprocessing(self):
        result = execute(
            'READ "../data/census.csv" (separator=",", header = 0, types = [1:numeric, 2:string]) AND\
            REPLACE (strategy = "mode", missing = "NaN", persist = "replace.csv" ) and\
            ENCODE (strategy = "regular", persist = "encode.csv" ) and\
            SPLIT (train = .8, test = 0.2, persist = [test:test.csv, train:train.csv])')
        assert os.path.isfile('replace.csv')
        os.remove('replace.csv')
        assert os.path.isfile('encode.csv')
        os.remove('encode.csv')
        assert os.path.isfile('test.csv')
        os.remove('test.csv')
        assert os.path.isfile('train.csv')
        os.remove('train.csv')



if __name__ == '__main__':
    unittest.main()
