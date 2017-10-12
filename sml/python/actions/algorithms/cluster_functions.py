"""
Performs logic to handle the CLUSTER keyword from ML-SQL language
"""
from ...utils import string_helpers
from .algorithms import handle_cluster_algorithm
from sklearn.feature_selection import SelectFromModel, RFE


def handle_cluster(data, algorithm, preds, label = None, clusters = 3, feature='RFE'):
    """
    Performs logic to handle the CLUSTER keyword from ML-SQL language
    """
    model = handle_cluster_algorithm(algorithm)
    if model is not None:
        #convert list of columns to integers and covert columns to start at 0
        if string_helpers.check_exists(label):
            pred_cols = list()
            for pred in preds:
                pred_cols.append(int(pred) - 1)
            X = data.iloc[:,pred_cols]
            label_col = string_helpers.convert_int(label) - 1
            y = data.iloc[:,label_col]
            return model.fit(X,y)
        else:
            return model.fit(data)
    else:
        return None


def _cluster_label(data, model, preds, label, feature):
    """
    Dataflow for clustering when a label is specified
    """
    #Convert label from a string to an int
    label_col = string_helpers.convert_int(label) - 1
    y = data.iloc[:,label_col]


    if feature is None or feature == 'RFE':
        try:
            feat_select = RFE(model) # Param for how many features the user wants
            feat_select.fit(X_train, y_train)
            #X_train = feat_select.transform(X_train)
            #X_test = feat_select.transform(X_test)
            return feat_select, X_train, y_train, X_test, y_test
        except RuntimeError:
            print ('Warning: This model does not have feature importance attributes (Using all features).')
        except ValueError:
            print ('Warning: This model does not have feature importance attributes (Using all features).')

    #Train model
    model.fit(X_train, y_train)

    return model, X_train, y_train, X_test, y_test


def handle_regress(data, algorithm, preds, label, feature='RFE'):
    """
    Performs logic to handle the classify keyword from ML-SQL language
    """
    model = handle_regress_algorithm(algorithm)
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
