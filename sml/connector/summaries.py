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

def summary_msg(parsingInfo, df, verbose=False):
    # Read keywords
    fileName = 'None'
    sep = 'None'

    # Split Keywords
    train = 'None'
    test = 'None'

    # Algorithm keywords
    predictors = 'None'
    label = 'None'
    algo = 'None'

    if parsingInfo.get('read') is not None:  

        filename = parsingInfo.get('read').get('fileName')
        sep = parsingInfo.get('read').get('sep')

        if parsingInfo.get('split') is not None:  # Since something was read in, it can be split
          train = float(parsingInfo.get('split').get('train_split')) * 100
          train = "%.2f%%" % train
          test = float(parsingInfo.get('split').get('test_split')) * 100
          test = "%.2f%%" % test

    algoType = get_algo(parsingInfo)

    if parsingInfo.get(algoType) is not None:

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
   Dataset Path:        %s
   Delimiter:      %s
   Training Set Split:       %s
   Testing Set Split:        %s
   Predictiors:        %s
   Label:         %s
   Algorithm:     %s
   Dataset Preview:
%s

=============================================
=============================================
''' % (filename, sep, train, test, predictors, label, algo, df.head()))
    else:
        print ('Using %s Algorithm, the dataset is from: %s. Currently using Predictors from column(s) %s and Label(s) from column(s) %s. ' \
        % (algo, filename, predictors, label) )
