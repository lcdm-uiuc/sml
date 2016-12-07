"""
Processes input after it has been parsed. Performs the dataflow for input.
"""
import numpy as np

from .summaries import *
from .util import *

def handle(parsing, verbose):
    '''
    :parsing - Parsed pyparsing object
    :verbose - boolean variable used to control type of messaged displayed to console
    Main Function that handles model phase, apply phase, and metric phase of SML
    '''

    keywords = keyword_check(parsing)

    model, df, X_train, y_train, X_test, y_test, algoType = _model_phase(keywords, verbose)

    if model is not None:  # If model isn't created no need to run through apply phase
        result = _apply_phase(keywords, model, X_test, y_test)

    if keywords.get('plot'):  # for now plot is the only thing that needs to be specified
        _metrics_phase(keywords, model, algoType, df, X_train, y_train, X_test, y_test)

def _model_phase(keywords, verbose=False):
    '''
    Used to build model.
    :keywords - Dictionary of SML keywords
    :returns (Nothing or the model, dataset, training and testing data split, and the algorithm of the model)
    '''
    if keywords.get('load') and keywords.get('read'):
        print('Cannot Execute both LOAD and READ on same query')
        return None, None, None, None, None, None, None

    if keywords.get('load'):
        return _connect_load(keywords, verbose)

    elif keywords.get('read'):

        df = _connect_read(keywords, verbose)
        model,X_train, y_train, X_test,y_test, algoType = _connect_model(df, keywords, verbose)

        if keywords.get('save') and model is not None:
            from ..python.actions.IO.modelIO import save_model
            fileName = keywords.get('save').get('savefile')
            save_model(fileName, model)
        return model, df, X_train, y_train, X_test, y_test, algoType

    else:
        print('No READ or LOAD keyword found')
        return None, None, None, None, None, None, None


def _connect_load(keywords, verbose):
    '''
    Loads Model from .sml file
    :keywords - Dictionary of SML keywords
    :returns the model
    '''
    from ..python.actions.IO.load_functions import handle_load
    model = handle_load(keywords.get('load').get('filename'))

    return model, None, None, None, None, None, None, None

def _connect_read(keywords, verbose):
    '''
    Reads data from READ Keyword
    :keywords - Dictionary of SML keywords
    :verbose - Boolean variable that controls how messages are displayed
    :returns pandas dataframe
    '''

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
    '''
    Trains model.
    :df - panadas dataframe
    keywords - dictionary of keywords
    verbose - boolean var that controls how messaged are displayed
    '''

    splitDict = keywords.get('split')
    split = not (splitDict == None)
    algoType = get_algo(keywords)

    if algoType == 'none':
        print("Warning: model not built since CLASSIFY, REGRESS, or CLUSTER not specified")
        summary_msg(keywords, df, verbose)
        return None, None, None, None, None, None

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
        mod, X_train, y_train, X_test, y_test = handle_classify(df, algorithm, predictors, label, split, train)
        summary_msg(keywords, df, verbose)
        return mod, X_train, y_train, X_test, y_test, algoType

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
        mod, X_train, y_train, X_test, y_test = handle_regress(df, algorithm, predictors, label, split, train)
        summary_msg(keywords, df, verbose)
        return mod, X_train, y_train, X_test, y_test, algoType

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
        mod, X_train, y_train, X_test, y_test = handle_cluster(df, algorithm, predictors, label, clusters, split, train)
        summary_msg(keywords, df, verbose)
        return mod, X_train, y_train, X_test, y_test, algoType

    else:
        print("Error: two or more of the keywords cluster, classify, and regress are in the query")
        return None, None, None, None, None, None

def _apply_phase(keywords, model, X_test, y_test):
    """
    Apply phase of SML used to label new data with the trained model
    Uses SML keywords: SPLIT, APPLY
    :keywords - dictionary of keywords and there values
    :model - trained model to apply to testing set
    :X_test - df of features to use
    :y_test - labels
    """
    if keywords.get('split'):
        results = model.score(X_test, y_test)
        return(results)
    if keywords.get('apply'):
        applyFile =  keywords.get('apply').get('applyFileName')
        print(applyFile)

    #classify = handle_classify(data, algo, predictors, label)
    pass


def _metrics_phase(keywords, model, algoType, df, X_train, y_train, X_test, y_test):
    '''
    Metrics phase of SML used to visualize data and results of model
    :keywords - dictionary of keywords and there values
    :model - trained model.
    :algoType - Type of Algorithm used.
    :df - pandas df used
    :X_train - training data (features)
    :y_train - training data (labels)
    :X_test - testing data (features)
    :y_test - testig=ng data (labels)
    '''

    plot_types = []

    from ..python.actions.metrics.visualize import handle_plots

    if model is None:  # Only Lattice Plot available
        if keyword.get('plot_type_values').lower() == 'auto' or keyword.get('plot_type_values').lower() == 'lattice':
            plot_types.append('lattice')

    else:  # More Options available to user with model
        if keywords.get('plot').get('plot_model_type').lower() == 'auto':# and algoType is not None: # Selected AUTO
            if algoType == 'classify':
                plot_types.extend(['lattice','ROC']) # 'learnCurves', 'validationCurves'
            elif algoType == 'regress':
                plot_types.extend(['lattice', 'learnCurves', 'validationCurves'])
            elif algoType == 'cluster':
                plot_types.extend(['lattice', 'learnCurves', 'validationCurves'])

    handle_plots(plot_types, keywords, algoType, model, df, X_train, y_train, X_test, y_test)
