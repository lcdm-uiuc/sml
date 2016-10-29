from .util import *

def summary_read(parsingInfo,df, verbose=False):
    filename = parsingInfo.get('read').get('fileName')
    sep = parsingInfo.get('read').get('sep')
    if verbose:
        print (\
'''
Sml Summary:
=============================================
=============================================
   Dataset:        %s
   Delimiter:      %s
   Dataset Preview\
   
   %s

=============================================
=============================================
''' % (filename, sep, df.head() ))
    else:
        print ('Using %s Algorithm, the dataset is from: %s. Currently using Predictors from column(s) %s and Label(s) from column(s) %s. ' \
        % (algo, filename, predictors, label) )


    return None

def summary_msg(parsingInfo, verbose=False):
    if parsingInfo.get('read') is None:
        fileName = 'None'
        sep = 'None'
    else:
        filename = parsingInfo.get('read').get('fileName')
        sep = parsingInfo.get('read').get('sep')
    if parsingInfo.get('read') is None:
        train = 'None'
        test = 'None'
    else:
        train = parsingInfo.get('split').get('train_split')
        test = parsingInfo.get('split').get('test_split')

    algoType = get_algo(parsingInfo)
    if parsingInfo.get(algoType) is None:
        predictors = 'None'
        label = 'None'
        algo = 'None'
    else:
        predictors = parsingInfo.get(algoType).get('predictors')
        label = parsingInfo.get(algoType).get('label')
        algo = parsingInfo.get(algoType).get('algorithm')

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
