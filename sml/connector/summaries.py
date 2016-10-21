



def summary_read(parsingInfo, verbose=False):
    filename = parsingInfo.get('read').get('fileName')
    sep = parsingInfo.get('read').get('set')
    return None
    
def summary_msg(parsingInfo, verbose=False):
    filename = parsingInfo.get('read').get('fileName')
    sep = parsingInfo.get('read').get('set')
    train = parsingInfo.get('split').get('train_split')
    test = parsingInfo.get('split').get('test_split')
    predictors = parsingInfo.get('algorithm').get('predictors')
    label = parsingInfo.get('algorithm').get('label')
    algo = parsingInfo.get('algorithm').get('algorithm')

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
