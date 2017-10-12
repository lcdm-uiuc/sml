from sml.python.actions.preprocessing.split_functions import handle_split

def process_data(keywords, verbose):
    if keywords.get('load') and keywords.get('read'):
        print('Cannot Execute both LOAD and READ on same query')
        return None, None, None, None
    elif keywords.get('read'):
        df = _connect_read(keywords, verbose)
        if keywords.get('replace'):
            df = _connect_replace(df, keywords, verbose)
        if keywords.get('encode'):
            df = _connect_encode(df, keywords, verbose)
        if keywords.get('split'):
            train_data, test_data = _connect_test_train_split(df, keywords)
        return df, train_data, test_data
    elif keywords.get('load'):
        return None, None, None, None
    else:
        msg = 'Error: No READ or LOAD keyword found'
        print(msg)



def _connect_read(keywords, verbose):
    '''
    Reads data from READ Keyword
    :keywords - Dictionary of SML keywords
    :verbose - Boolean variable that controls how messages are displayed
    :returns pandas dataframe
    '''
    import sml.python.actions.preprocessing as pp
    readDict = keywords.get('read')
    df = pp.handle_read(readDict.get('fileName'), readDict.get('sep'),\
    readDict.get('header'), readDict.get('dtypes'))

    return df

def _connect_replace(df, keywords, verbose):
    import sml.python.actions.preprocessing as pp
    import sml.python.actions.IO as io
    replaceDict = keywords.get('replace')
    replaces = list()
    replaces.append(None)
    replaces.append(replaceDict.get('replaceIdentifier'))
    replaces.append(replaceDict.get('replaceValue'))
    df = pp.handle_replace(df, replaces)
    if replaceDict.get('replacePersist'):
        io.handle_write_csv(df, replaceDict.get('replacePersist'))
    return df

def _connect_encode(df, keywords, verbose):
    import sml.python.actions.preprocessing as pp
    import sml.python.actions.IO as io

    encodeDict = keywords.get('encode')
    strategy = encodeDict.get('encodeStrategy')
    pp.handle_encode(strategy, df)
    if encodeDict.get('encodePersist'):
        io.handle_write_csv(df, encodeDict.get('encodePersist'))
    return df

def _connect_test_train_split(df,keywords):
    import sml.python.actions.preprocessing as pp
    import sml.python.actions.IO as io
    splitDict = keywords.get('split')
    train = splitDict.get('train_split')
    train_data, test_data = handle_split(df,train)
    persist_names = splitDict.get('persist_names_split')
    if persist_names is not None:
        test_name, train_name = _get_test_train_names(persist_names)
        io.handle_write_csv(test_data, test_name)
        io.handle_write_csv(train_data, train_name)
        return train_data, test_data
    else:
        return train_data, test_data

def _get_test_train_names(persist_names):
    persist_names = str(persist_names)
    persist_names = persist_names.replace('[', '')
    persist_names = persist_names.replace(']', '')
    persist_names = persist_names.replace('\'','')
    persist_names = persist_names.replace(' ', '')
    persist_list = persist_names.split(',')
    for pair in persist_list:
        elem = pair.split(':')
        if elem[0] == 'test':
            test = elem[1]
        elif elem[0] == 'train':
            train = elem[1]
    return test,train
