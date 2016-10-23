_keywords = {
            'load':['fileName'],
            'read':['fileName', 'header', 'sep', 'dtypes'],
            'split':['train_split','test_split'],
            'replace':['replaceColumns','replaceValue','replaceIdentifier'],
            'classify': ['predictors', 'label', 'algorithm'],
            'regress': ['predictors', 'label', 'algorithm'],
            'cluster': ['predictors', 'label', 'numClusters'],
            'save': ['savefile']
             }
_listOptions = ['predictors', 'dtypes']

def keyword_check(parsing):
    keys = {}
    for key in _keywords:
        parse_check = None
        try:
            parse_check = parsing[key]
        except KeyError:
            parse_check = ""
        if (parse_check is not None) and (parse_check != ""):
            keys[key] = {}
            for innerKey in _keywords[key]:
                try:
                    if innerKey in _listOptions:
                        keys[key][innerKey] = [x.strip() for x in parsing[innerKey].split(',')]
                    else:
                        keys[key][innerKey] = parsing[innerKey]
                except KeyError:
                    keys[key][innerKey] = None
            if keys[key] == {}:
                keys[key] = True
        else:
            keys[key] = None
    return keys
