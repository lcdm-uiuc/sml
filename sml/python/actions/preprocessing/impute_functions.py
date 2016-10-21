import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.preprocessing import Imputer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.ensemble import RandomForestRegressor
import re

def handle_replace(dataframe, item):
    ret = dataframe

    missingVal = item[1]
    strategy = item[2]
    ret = _impute_missing(data=dataframe, columns = None,\
    impute_strategy=strategy, missing_values = missingVal)

    return ret

"""
impute_missing()
Parameters:
  data: Dataframe to impute missing values on
  columns: Columns to impute. If None, impute all columns
  impute_strategy: What to replace missing values with
     Options:
      Imputer Class
      'mode' -  numerical and objects
      'median' - numerical
      'mean' - numerical
      'maximum' - numerical
      'minimum' - numerical
      Custom Functions
      'remove'
      'dummy'
      'rand_forest_reg'
Returns: Imputed dataframe
"""
def _impute_missing(data, columns=None, impute_strategy='mode', missing_values='NaN'):
    datacopy = data
    dummy_val = 'U0'
    cols_to_impute = list()

    data = data.replace(missing_values, np.nan)

    if columns == None:
        cols_to_impute = _find_cols_with_missing_vals(data)
    else:
        cols_to_impute = columns
    if not cols_to_impute:
        return datacopy
    else:
        if impute_strategy == 'mode':
            for col in cols_to_impute:
                modeVal = data[col].mode()
                if len(modeVal) == 0:
                    print('Invalid Value of Mode in column: ' + col)
                    print(data[col])
                    continue
                datacopy[col] = _fill_col(data[col], modeVal[0])
            return datacopy
        elif impute_strategy == 'mean':
            for col in cols_to_impute:
                if data[col].dtype != 'object':
                    meanVal = data[col].mean()
                    datacopy[col] = _fill_col(data[col], meanVal)
                else:
                    datacopy[col] = _fill_col(data[col], dummy_val)
                    print("CANNOT USE COLUMN " + str(col)+" FOR MEAN IMPUTATION STRATEGY, DUMMY VALUE OF "+ dummy_val + " USED")
            return datacopy
        elif impute_strategy == 'median':
            for col in cols_to_impute:
                if data[col].dtype != 'object':
                    medianVal = data[col].median()
                    datacopy[col] = _fill_col(data[col], medianVal)
                else:
                    datacopy[col] = _fill_col(data[col], dummy_val)
                    print("CANNOT USE COLUMN" + str(col) + " FOR MEDIAN IMPUTATION STRATEGY, DUMMY VALUE OF "+ dummy_val + " USED")
            return datacopy
        elif impute_strategy == 'drop column':
            return _remove_columns(data, cols_to_impute)
        elif impute_strategy == 'maximum':
            for col in cols_to_impute:
                if data[col].dtype != 'object':
                    maxVal = max(data[col])
                    datacopy[col] = _fill_col(data[col], maxVal)
                else:
                    datacopy[col] =  _fill_col(data[col], dummy_val)
                    print("CANNOT USE COLUMN " + str(col) + " FOR MAXIMUM IMPUTATION STRATEGY, DUMMY VALUE OF "+ dummy_val + " USED")
            return datacopy
        elif impute_strategy == 'minimum':
            for col in cols_to_impute:
                if data[col].dtype != 'object':
                    minVal = min(data[col])
                    datacopy[col] = _fill_col(data[col], minVal)
                else:
                    datacopy[col] = _fill_col(data[col], dummy_val)
                    print("CANNOT USE COLUMN " + str(col)+ " FOR MINIMUM IMPUTATION STRATEGY, DUMMY VALUE OF "+ dummy_val + " USED")
            return datacopy
        elif impute_strategy == 'dummy':
            for col in cols_to_impute:
                if data[col].dtype != 'object':
                    datacopy[col] = _fill_col(data[col], 0)
                else:
                    datacopy[col] = _fill_col(data[col], dummy_val)
            return datacopy
      # Do some more research on this before implementing
        elif impute_strategy == 'rand_forest_reg':
            print("RANDOM FOREST REGRESSOR NOT IMPLEMENTED NO IMPUTATION HAPPENED")
            return datacopy
        else:
            print ("REPLACE COMMAND NOT RECOGNIZED NO IMPUTATION HAPPENED")
            return datacopy

"""
remove_columns()
Parameters:
  data: dataframe to remove columns
  delete_list: list of names of columns to delete
Returns:
  Dataframe with deleted columns
"""
def _remove_columns(data, delete_list):
  for col in delete_list:
      del data[col]
  return data

def _find_cols_with_missing_vals(data=None):
    cols_to_impute = list()
    for col in data.columns:
        if data[col].isnull().values.any():
            cols_to_impute.append(col)
    return cols_to_impute

def _fill_col(column, replace_val):
    ret = column
    ret = column.fillna(replace_val)
    return ret
