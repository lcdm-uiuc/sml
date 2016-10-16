"""
Performs logic to handle the read keyword from ML-SQL language
"""

from ..utils.modelIO import load_model
from ..utils.filepath import is_mlsql_file, file_exists

def handle_read(userfile, separator, header,types = None):
    """
    Main exported function
    Performs logic to handle the read keyword from ML-SQL language
    """
    if is_mlsql_file(userfile):
        model = load_model(userfile)
    else:
        return _read_data_file(userfile, separator, header, types)


def _read_data_file(userfile, separator, header, types=None):
    """
    Reads a CSV-like file from memory with options for header and separator
    """
    if not file_exists:
        return None
    from pandas import read_csv

    #create dataframe for read in file
    df = None

    #handle different parameters for read
    head = _handle_header(header)
    separ = _handle_separator(separator)
    dtypes = _handle_dtypes(types)

    #attempt to read file with given parameters
    try:
        if head is None:
            df = read_csv(userfile, sep=separ, header=None)
        else:
            df = read_csv(userfile, sep = separ, header = head)

    except OSError as e:
        print("Error importing file: '" + userfile + "'")
        print(e)
        return None
    if dtypes is not None:
        df = _change_types(df, dtypes)
    return (df)


def _handle_header(header):
    """
    Translates header into a proper value to be read by read_csv functions from pandas
    """

    if header is None or header == "" or header == "None":
        return None
    elif header == "False":
        return None
    elif header == "True":
        return 0
    else:
        try:
            #check if header can be parsed to an int
            result = int(header)
            return result
        except ValueError as v:
            return None
        return 0


def _handle_separator(sep):
    """
    Translates separator into a proper value to be read by read_csv functions from pandas
    """
    if sep is None or sep == "":
        return ","
    else:
        return str(sep)

def _handle_dtypes(dtypes):
    """
    Translates datatypes into a list of [<index>:<type>] strings
    """
    if dtypes == None:
        return None
    dtypes = str(dtypes)
    dtypes = dtypes.replace('[', '')
    dtypes = dtypes.replace(']', '')
    dtypes = dtypes.replace('\'','')
    dtypes = dtypes.replace(' ', '')
    ret = dtypes.split(',')
    return ret

def _change_types(df, dtypes):
    import pandas as pd
    """
    Change datatypes according to data type specification
    """
    ret = df
    cols = ret.columns
    for element in dtypes:
        elemList = element.split(':')
        index = int(elemList[0])
        dtype = elemList[1]
        if dtype == 'numeric':
            ret[cols[index - 1]] = pd.to_numeric(ret[cols[index - 1]], errors='coerce')
        if dtype == 'string':
            ret[cols[index - 1]] = ret[cols[index - 1]].astype(str)

    return ret
