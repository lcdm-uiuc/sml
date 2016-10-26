"""
Processes input after it has been parsed. Performs the dataflow for input.
"""
import numpy as np

from .summaries import *
from .util import *



def handle(parsing, verbose):
    keywords = keyword_check(parsing)
    summary_msg(keywords, verbose)
    model, X_test, y_test = _model_phase(keywords, verbose)

def _model_phase(keywords, verbose=False):
    if keywords.get('load') and keywords.get('read'):
        print('Cannot Execute both LOAD and READ on same query')
        return None, None, None

    if keywords.get('load'):
        return _connect_load(keywords, verbose)
    elif keywords.get('read'):
        df = _connect_read(keywords, verbose)
        return _connect_model(df, keywords)
        return None, None, None
    else:
        print('No READ or LOAD keyword found')
        return None, None, None


def _connect_load(keywords, verbose):
    from ..python.actions.IO.load_functions import handle_load
    model = handle_load(keywords.get('load').get('fileName'))
    return model, None, None


def _connect_read(keywords,verbose):
    from ..python.actions.preprocessing.read_functions import handle_read
    from ..python.actions.preprocessing.encode_functions import encode_categorical
    readDict = keywords.get('read')
    df = handle_read(readDict.get('fileName'), readDict.get('sep'),\
    readDict.get('header'), readDict.get('dtypes'))
    if keywords.get('replace'):
        replaceDict = keywords.get('replace')
        from ..python.actions.preprocessing.impute_functions import handle_replace
        replaces = list()
        replaces.append(None)
        replaces.append(replaceDict.get('replaceIdentifier'))
        replaces.append(replaceDict.get('replaceValue'))
        df = handle_replace(df, replaces)
    df = encode_categorical(df)
    return df

def _connect_model(df, keywords):
    splitDict = keywords.get('split')
    if splitDict == None:
        split = False
    else:
        split = True
    train = keywords.get('split').get('train_split')
    algoType = get_algo(keywords)
    #Classification and Regression and Cluster
    if algoType == 'none':
        print("Warning: model cannot be built since CLASSIFY, REGRESS, or CLUSTER not specified")
        return None, None, None
    elif algoType == 'classify':
        from ..python.actions.algorithms.classify_functions import handle_classify
        algoDict = keywords.get('classify')
        algorithm = algoDict.get('algorithm')
        predictors = algoDict.get('predictors')
        label = algoDict.get('label')
        mod, X_test, y_test = handle_classify(df, algorithm, predictors, label, split, train)
        return mod, X_test, y_test

    elif algoType == 'regress':
        from ..python.actions.algorithms.regress_functions import handle_regress
        algoDict = keywords.get('regress')
        algorithm = algoDict.get('algorithm')
        predictors = algoDict.get('predictors')
        label = algoDict.get('label')
        mod, X_test, y_test = handle_regress(df, algorithm, predictors, label, split, train)
        return mod, X_test, y_test

    elif algoType == 'cluster':
        from ..python.actions.algorithms.cluster_functions import handle_cluster
        algoDict = keywords.get('cluster')
        algorithm = algoDict.get('algorithm')
        predictors = algoDict.get('predictors')
        label = algoDict.get('label')
        clusters = algoDict.get('numClusters')
        mod, X_test, y_test = handle_cluster(df, algorithm, predictors, label, clusters, split, train)
        return mod, X_test, y_test

    else:
        print("Error: two or more of the keywords cluster, classify, and regress are in the query")
        return None, None, None



# def _model_phase(keywords, filename, header, sep, train, predictors, label, algorithm, replace = None, clusters = None, verbose=False, types=None):
#     """
#     Model phase of ML-SQL used to create a model
#     Uses ML-SQL keywords: READ, REPLACE, SPLIT, CLASSIFY, REGRESSION
#     """
#     #load keyword
#     if keywords["load"]:
#         from .keywords.load_functions import handle_load
#         model = handle_load(filename)
#         return model, None, None
#     #read file
#     df = None
#     if keywords["read"]:
#         from .keywords.read_functions import handle_read
#         if keywords['dtypes']:
#             df = handle_read(filename, sep, header, types)
#         else:
#             df = handle_read(filename, sep, header)
#
#         if df is not None and verbose is True:
#             #Data was read in properly
#
#             print(\
# """
# Header of Dataset (%s):
# =============================================
# =============================================
# %s
# =============================================
# =============================================""" % (filename, df.head()) )
#     #Replace
#     if keywords["replace"]:
#         from .keywords.replace_functions import handle_replace
#         df = handle_replace(df, [replace])
#
#
#         if df is not None and verbose is True:
#             #Data was read in properly
#             print(\
# """
# Updated Dataset (%s):
# =============================================
# =============================================
#         %s
# =============================================
# =============================================""" % (filename, df.head()) )
#     # Encode all categorical values
#     df = encode_categorical(df)
#     #Classification and Regression and Cluster
#     if not keywords["classify"] and not keywords["regress"] and not keywords["cluster"]:
#         # KI: Rationale behind changining Error to Warning is that the user may
#         # Want to just read data...
#         print("Warning: model cannot be built since CLASSIFY, REGRESS, or CLUSTER not specified")
#         return None, None, None
#
#     elif keywords["classify"] and not keywords["regress"] and not keywords["cluster"]:
#         from .keywords.classify_functions import handle_classify
#         mod, X_test, y_test = handle_classify(df, algorithm, predictors, label, keywords["split"], train)
#         return mod, X_test, y_test
#
#     elif not keywords["classify"] and keywords["regress"] and not keywords["cluster"]:
#         from .keywords.regress_functions import handle_regress
#         mod, X_test, y_test = handle_regress(df, algorithm, predictors, label, keywords["split"], train)
#         return mod, X_test, y_test
#
#     elif not keywords["classify"] and not keywords["regress"] and keywords["cluster"]:
#         from .keywords.cluster_functions import handle_cluster
#         mod, X_test, y_test = handle_cluster(df, algorithm, predictors, label, clusters, keywords["split"], train)
#         return mod, X_test, y_test
#
#     else:
#         print("Error: two or more of the keywords cluster, classify, and regress are in the query")
#         return None, None, None
#
#
# def _apply_phase(keywords):
#     """
#     Apply phase of ML-SQL used to label new data with the trained model
#     Uses ML-SQL keywords: SPLIT, APPLY
#     """
#     #classify = handle_classify(data, algo, predictors, label)
#     pass
#
#
# def _metrics_phase(model, X_test, y_test):
#     """
#     Metrics phase of ML-SQL used to calculate or plot results
#     Uses ML-SQL keywords: PLOT, CALCULATE, GRAPH
#     """
#     #Performance on test data
#     if X_test is not None and y_test is not None:
#         print("Testing Accuracy: %.2f%%" % (model.score(X_test, y_test) * 100))
#     else:
#         return None
