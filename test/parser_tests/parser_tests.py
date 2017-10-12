import unittest
import sys
import traceback
from sml.parser import smlparser
import numpy as np

class parser_tests(unittest.TestCase):
    _keywords = {
                'load':['fileName'],
                'read':['fileName', 'header', 'sep', 'dtypes'],
                'split':['train_split','test_split','persist_names_split'],
                'replace':['replaceColumns','replaceValue','replaceIdentifier','replacePersist'],
                'classify': ['predictors', 'label', 'algorithm', 'feature'],
                'regress': ['predictors', 'label', 'algorithm', 'feature'],
                'cluster': ['predictors', 'label', 'numClusters','algorithm', 'feature'],
                'save': ['savefile'],
                'encode':['encodeStrategy', 'encodePersist'],
                'apply':['applyFileName', 'applyHeader', 'applySep', 'applyDTypes','applyPredictors','applyLabel'],
                'plot':['plot_model_type', 'plot_type_values']
                 }
    _listOptions = ['predictors', 'dtypes','applyDTypes','persist_names_split','applyPredictors']
    def keyword_check(self,parsing):
        '''
        Maps parsed string to dictionary
        :returns dictionary of keywords with values from Query.
        '''

        keys = {}
        for key in self._keywords:
            parse_check = None
            try:
                parse_check = parsing[key]
            except KeyError:
                parse_check = ""
            if (parse_check is not None) and (parse_check != ""):
                keys[key] = {}
                for innerKey in self._keywords[key]:
                    try:
                        if innerKey in self._listOptions:
                            keys[key][innerKey] = [x.strip() for x in parsing[innerKey].split(',')]
                        else:
                            keys[key][innerKey] = parsing[innerKey]
                    except KeyError:
                        keys[key][innerKey] = None
                if keys[key] == {}:
                    keys[key] = True
            else:
                keys[key] = None
        return keys

    def test_boston_full(self):
        test = {
        'regress': {'predictors': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'], 'algorithm': 'elastic', 'feature': None, 'label': '14'},
        'split': {'train_split': '.8', 'test_split': '.2', 'persist_names_split': None},
        'classify': None,
        'cluster': None,
        'apply': None,
        'load': None,
        'replace': None,
        'encode': None,
        'read': {'sep': '\\s+', 'dtypes': None, 'header': '0', 'fileName': '../data/boston.csv'},
        'save': None,
        'plot': None
        }

        myparser = smlparser()
        parsed = myparser.parseString(
            'READ "../data/boston.csv" (separator = "\s+", header = 0) AND\
            SPLIT (train = .8, test = .2, validation = .0) AND\
            REGRESS (predictors = [1,2,3,4,5,6,7,8,9,10,11,12,13], label = 14, algorithm = elastic)')

        result = self.keyword_check(parsed)
        assert test == result

    def test_full_preprocessing(self):
        myparser = smlparser()
        test = {
            'load': None,
            'read': {'header': '0', 'fileName': '../data/census.csv', 'sep': ',', 'dtypes': ['1:numeric', '2:string']},
            'plot': None,
            'regress': None,
            'apply': None,
            'cluster': None,
            'replace': {'replaceColumns': None, 'replaceValue': 'mode', 'replaceIdentifier': 'NaN','replacePersist': "replace.csv"},
            'split': {'test_split': '0.2', 'train_split': '.8','persist_names_split': ['test:test.csv', 'train:train.csv']},
            'encode': {'encodeStrategy': 'regular', 'encodePersist': 'encode.csv'},
            'classify': None,
            'save': None,
        }

        parsed = myparser.parseString(
            'READ "../data/census.csv" (separator=",", header = 0, types = [1:numeric, 2:string]) AND\
            REPLACE (strategy = "mode", missing = "NaN", persist = "replace.csv" ) and\
            ENCODE (strategy = "regular", persist = "encode.csv" ) and\
            SPLIT (train = .8, test = 0.2, persist = [test:test.csv, train:train.csv])')

        result = self.keyword_check(parsed)

        assert test == result
    def test_model_building(self):
        myparser = smlparser()

        test = {
            'load': None,
            'read': {'header': None, 'fileName': '../data/auto.csv', 'sep': '\\s+', 'dtypes': None},
            'plot': None,
            'regress': {'predictors': ['2', '3', '4', '5', '6', '7', '8'], 'algorithm': 'lasso', 'feature': None, 'label': '1'},
            'apply': None,
            'cluster': None,
            'replace': None,
            'split': {'test_split': '.2', 'train_split': '.8','persist_names_split': None},
            'encode': None,
            'classify': None,
            'save': None,
        }
        query ='READ "../data/auto.csv" (separator = "\s+") AND\
          SPLIT (train = .8, test = .2) AND \
          REGRESS (predictors = [2,3,4,5,6,7,8], label = 1, algorithm = lasso)'
        parsed = myparser.parseString(query)
        result = self.keyword_check(parsed)

        assert test == result

    def test_apply(self):
        myparser = smlparser()

        query ='READ "../data/auto.csv" (separator = "\s+") AND\
          SPLIT (train = .8, test = .2) AND \
          REGRESS (predictors = [2,3,4,5,6,7,8], label = 1, algorithm = lasso) AND\
          APPLY "test.csv"(separator = "\s+", predictors = [2,3,4,5,6,7,8], label = 1)'
        test = {
            'load': None,
            'read': {'header': None, 'fileName': '../data/auto.csv', 'sep': '\\s+', 'dtypes': None},
            'plot': None,
            'regress': {'predictors': ['2', '3', '4', '5', '6', '7', '8'], 'algorithm': 'lasso', 'feature': None, 'label': '1'},
            'apply': {'applyFileName':'test.csv','applyHeader' : None, 'applySep':'\\s+','applyDTypes': None, 'applyPredictors': ['2', '3', '4', '5', '6', '7', '8'], 'applyLabel': '1'},
            'cluster': None,
            'replace': None,
            'split': {'test_split': '.2', 'train_split': '.8','persist_names_split': None},
            'encode': None,
            'classify': None,
            'save': None,
        }
        parsed = myparser.parseString(query)
        result = self.keyword_check(parsed)

        assert test == result

if __name__ == '__main__':
    unittest.main()
