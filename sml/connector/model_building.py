from .summaries import *
from .util import *
def build_model(keywords, data_train, verbose=False):
    '''
    Used to build model.
    :keywords - Dictionary of SML keywords
    :returns (Nothing or the model and the algorithm of the model)
    '''
    if keywords.get('load'):
        return _connect_load(keywords, verbose)
    model, algoType, msg = _connect_model(data_train, keywords, verbose)

    if keywords.get('save') and model is not None:
        from ..python.actions.IO.modelIO import save_model
        fileName = keywords.get('save').get('savefile')
        save_model(fileName, model)
    return model, algoType, msg

def _connect_load(keywords, verbose):
    '''
    Loads Model from .sml file
    :keywords - Dictionary of SML keywords
    :returns the model
    '''
    from ..python.actions.IO.load_functions import handle_load
    model = handle_load(keywords.get('load').get('fileName'))
    return model, None, None



def _connect_model(df, keywords, verbose=False):
    '''
    Trains model.
    :df - panadas dataframe
    keywords - dictionary of keywords
    verbose - boolean var that controls how messaged are displayed
    '''

    algoType = get_algo(keywords)

    if algoType == 'none':
        print("Warning: model not built since CLASSIFY, REGRESS, or CLUSTER not specified")
        msg = summary_msg(keywords, df, verbose)
        return None, None, summary_msg

    elif algoType == 'classify':
        from ..python.actions.algorithms.classify_functions import handle_classify
        algoDict = keywords.get('classify')
        algorithm = algoDict.get('algorithm')
        predictors = algoDict.get('predictors')
        label = algoDict.get('label')
        mod = handle_classify(df, algorithm, predictors, label, keywords['classify']['feature'])
        msg = summary_msg(keywords, df, verbose)
        return mod, algoType, msg

    elif algoType == 'regress':
        from ..python.actions.algorithms.regress_functions import handle_regress
        algoDict = keywords.get('regress')
        algorithm = algoDict.get('algorithm')
        predictors = algoDict.get('predictors')
        label = algoDict.get('label')
        mod = handle_regress(df, algorithm, predictors, label, keywords['regress']['feature'])
        msg = summary_msg(keywords, df, verbose)
        return mod, algoType, msg

    elif algoType == 'cluster':
        from ..python.actions.algorithms.cluster_functions import handle_cluster
        algoDict = keywords.get('cluster')
        algorithm = algoDict.get('algorithm')
        predictors = algoDict.get('predictors')
        label = algoDict.get('label')
        clusters = algoDict.get('numClusters')
        mod = handle_cluster(df, algorithm, predictors, label, clusters, keywords['cluster']['feature'])
        msg = summary_msg(keywords, df, verbose)
        return mod, algoType, msg

    else:
        msg = "Error: two or more of the keywords cluster, classify, and regress are in the query"
        print(msg)
        return None, None, msg
