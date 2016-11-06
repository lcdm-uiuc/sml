"""
Processes input after it has been parsed. Performs the dataflow for input.
"""
import numpy as np

from .summaries import *
from .util import *



def handle(parsing, verbose):
    keywords = keyword_check(parsing)
    # print(keywords)
    model, X_test, y_test = _model_phase(keywords, verbose)

    if model is not None:  # If model isn't created no need to run through apply phase
        result = _apply_phase(keywords, model, X_test, y_test)






def _model_phase(keywords, verbose=False):
    if keywords.get('load') and keywords.get('read'):

        # KI: Why?? They should load the model params and then use it for new data...
        print('Cannot Execute both LOAD and READ on same query')
        return None, None, None

    if keywords.get('load'):
        return _connect_load(keywords, verbose)
    elif keywords.get('read'):
        df = _connect_read(keywords, verbose)
        model,X_test,y_test = _connect_model(df, keywords, verbose)
        if keywords.get('save') and model is not None:
            from ..python.actions.IO.modelIO import save_model
            fileName = keywords.get('save').get('savefile')
            save_model(fileName, model)
        return model, X_test, y_test
    else:
        print('No READ or LOAD keyword found')
        return None, None, None


def _connect_load(keywords, verbose):
    from ..python.actions.IO.load_functions import handle_load
    model = handle_load(keywords.get('load').get('filename'))
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

def _connect_model(df, keywords, verbose=False):
    splitDict = keywords.get('split')
    split = not (splitDict == None)
    algoType = get_algo(keywords)
    if algoType == 'none':
        print("Warning: model not built since CLASSIFY, REGRESS, or CLUSTER not specified")
        summary_msg(keywords, df, verbose)
        return None, None, None
    elif algoType == 'classify':
        from ..python.actions.algorithms.classify_functions import handle_classify
        algoDict = keywords.get('classify')
        algorithm = algoDict.get('algorithm')
        predictors = algoDict.get('predictors')
        label = algoDict.get('label')
        if split:
            train = keywords.get('split').get('train_split')
        else:
            train = 1
        mod, X_test, y_test = handle_classify(df, algorithm, predictors, label, split, train)
        return mod, X_test, y_test

    elif algoType == 'regress':
        from ..python.actions.algorithms.regress_functions import handle_regress
        algoDict = keywords.get('regress')
        algorithm = algoDict.get('algorithm')
        predictors = algoDict.get('predictors')
        label = algoDict.get('label')
        if split:
            train = keywords.get('split').get('train_split')
        else:
            train = 1
        mod, X_test, y_test = handle_regress(df, algorithm, predictors, label, split, train)
        return mod, X_test, y_test

    elif algoType == 'cluster':
        from ..python.actions.algorithms.cluster_functions import handle_cluster
        algoDict = keywords.get('cluster')
        algorithm = algoDict.get('algorithm')
        predictors = algoDict.get('predictors')
        label = algoDict.get('label')
        clusters = algoDict.get('numClusters')
        if split:
            train = keywords.get('split').get('train_split')
        else:
            train = 1
        mod, X_test, y_test = handle_cluster(df, algorithm, predictors, label, clusters, split, train)
        return mod, X_test, y_test

    else:
        print("Error: two or more of the keywords cluster, classify, and regress are in the query")
        return None, None, None




def _apply_phase(keywords, model, X_test, y_test):
    """
    Apply phase of SML used to label new data with the trained model
    Uses SML keywords: SPLIT, APPLY
    """
    if keywords.get('split'):
        results = model.score(X_test, y_test)
        return(results)



    #classify = handle_classify(data, algo, predictors, label)
    pass

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
