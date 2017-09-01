from .summaries import *
from .util import *


def apply_model(keywords, model, X_test, y_test):
    """
    Apply phase of SML used to label new data with the trained model
    Uses SML keywords: SPLIT, APPLY
    :keywords - dictionary of keywords and there values
    :model - trained model to apply to testing set
    :X_test - df of features to use
    :y_test - labels
    """
    if keywords.get('split') and X_test is not None and y_test is not None:
        results = model.score(X_test, y_test)
        return(results)
    if keywords.get('apply'):
        from ..python.actions.preprocessing.read_functions import handle_read
        from ..python.actions.preprocessing.encode_functions import encode_categorical
        applyFile =  keywords.get('apply').get('applyFileName')
        readDict = keywords.get('read')
        # Assumption that testing file is in the same format as the original training file
        df = handle_read(applyFile, readDict.get('sep'),\
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

        algoDict = keywords.get('classify')
        predictors = algoDict.get('predictors')
        label = algoDict.get('label')
        X_test,y_test = split_dataframe(df, predictors, label)
        results = model.score(X_test, y_test)
        return(results)

    else:
        print("Apply phase could not be completed")
        return(None)
    pass
