"""
Performs logic to handle the CLASSIFY keyword from ML-SQL language
"""
from ...utils import string_helpers
from .algorithms import handle_classify_algorithm
from sklearn.feature_selection import SelectFromModel, RFE

def handle_classify(data, algorithm, preds, label, feature='RFE'):
    """
    Performs logic to handle the classify keyword from ML-SQL language
    """
    model = handle_classify_algorithm(algorithm)
    if model is not None:

        #convert list of columns to integers and covert columns to start at 0
        pred_cols = list()
        for pred in preds:
            pred_cols.append(int(pred) - 1)

        #Convert label from a string to an int
        label_col = string_helpers.convert_int(label) - 1

        X = data.iloc[:,pred_cols]
        y = data.iloc[:,label_col]

        #Train model
        model.fit(X, y)

        return model
    else:
        return None
