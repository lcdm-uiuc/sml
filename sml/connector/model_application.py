from .summaries import *
from .util import *

def apply_model(keywords, model, data):
    """
    Apply phase of SML used to label new data with the trained model
    Uses SML keywords: SPLIT, APPLY
    :keywords - dictionary of keywords and there values
    :model - trained model to apply to testing set
    :X_test - df of features to use
    :y_test - labels
    """
    if keywords.get('split'):
        algoType = get_algo(keywords)
        algoDict = keywords.get(algoType)
        predictors = algoDict.get('predictors')
        label = algoDict.get('label')
        pred_cols = list()
        for pred in predictors:
            pred_cols.append(int(pred) - 1)

        #Convert label from a string to an int
        label_col = int(label) - 1

        X_test = data.iloc[:,pred_cols]
        y_test = data.iloc[:,label_col]
        results = model.score(X_test, y_test)
        return(results)
    if keywords.get('apply'):
        from ..python.actions.preprocessing.read_functions import handle_read
        from ..python.actions.preprocessing.encode_functions import encode_categorical
        applyDict = keywords.get('apply')
        applyFile = applyDict.get('applyFileName')
        # Assumption that testing file is in the same format as the original training file
        df = handle_read(applyFile, applyDict.get('applySep'),\
        applyDict.get('applyHeader'), applyDict.get('applyDTypes'))
        if keywords.get('replace'):
            replaceDict = keywords.get('replace')
            from ..python.actions.preprocessing.impute_functions import handle_replace
            replaces = list()
            replaces.append(None)
            replaces.append(replaceDict.get('replaceIdentifier'))
            replaces.append(replaceDict.get('replaceValue'))
            df = handle_replace(df, replaces)
        df = encode_categorical(df)

        predictors = applyDict.get('applyPredictors')
        label = applyDict.get('applyLabel')
        X_test,y_test = split_dataframe(df, predictors, label)
        results = model.score(X_test, y_test)
        return(results)

    else:
        print("No apply phase")
        return(None)
    pass
