"""
Processes input after it has been parsed. Performs the dataflow for input.
"""
import numpy as np
from ..python.actions.preprocessing.read_functions import handle_read

keywords = {
            'load':['fileName'],
            'read':['fileName', 'header', 'sep', 'dtypes'],
            'split':['train_split','test_split'],
            'replace':['replaceColumns','replaceValue','replaceIdentifier',
            'replaceIdentifier','replaceValue'],
            'algorithm': ['predictors', 'label', 'algorithm'],
            'classify': [],
            'regress': [],
            'cluster': [],
            'save': ['savefile']
             }
listOptions = ['predictors', 'dtypes']

def handle(parsing, verbose):
    # create a dictionary with all keywords
    keywords_used = _keyword_check(parsing)
    print(keywords_used)
    # print out summary message
    summary_msg(keywords_used, verbose)
    handle_read('a','b','c')

def _keyword_check(parsing):
    keys = {}
    for key in keywords:
        parse_check = None
        try:
            parse_check = parsing[key]
        except KeyError:
            parse_check = ""
        if (parse_check is not None) and (parse_check != ""):
            keys[key] = {}
            for innerKey in keywords[key]:
                try:
                    if innerKey in listOptions:
                        keys[key][innerKey] = [x.strip() for x in parsing[innerKey].split(',')]
                    else:
                        keys[key][innerKey] = parsing[innerKey]
                except KeyError:
                    keys[key][innerKey] = None

    return keys

def summary_msg(parsingInfo, verbose=False):
    filename = parsingInfo['read']['fileName']
    sep = parsingInfo['read']['sep']
    train = parsingInfo['split']['train_split']
    test = parsingInfo['split']['test_split']
    predictors = parsingInfo['algorithm']['predictors']
    label = parsingInfo['algorithm']['label']
    algo = parsingInfo['algorithm']['algorithm']
    """
    Prints out detailed  summary message if verbose is True.
    Or simple summary message.
    """
    if verbose:
        print (\
'''
Sml Summary:
=============================================
=============================================
   Dataset:        %s
   Delimiter:      %s
   Training Set Split:       %.2f%%
   Testing Set Split:        %.2f%%
   Predictiors:        %s
   Label:         %s
   Algorithm:     %s
=============================================
=============================================
''' % (filename, sep, float(train)*100, float(test)*100, predictors, label, algo))
    else:
        print ('Using %s Algorithm, the dataset is from: %s. Currently using Predictors from column(s) %s and Label(s) from column(s) %s. ' \
        % (algo, filename, predictors, label) )



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
