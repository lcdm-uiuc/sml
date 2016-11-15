"""
Handles persisting models by saving and loading them into files
"""

from ...utils.filepath import get_model_type, get_relative_filename, file_exists
from ..algorithms.algorithms import check_all
import json
from collections import OrderedDict,namedtuple
import numpy as np

# Constant defining how a file is split into separate components
SEP = ";"
EXTENSION = ".sml"

def save_model(filename, model):
    """
    Save a model that has already been trained into a .sml file
    The file is saved to the current working directory with the name of the file
    """

    relative_file = get_relative_filename(filename)

    #ensure file does not already exist, if it does, program will add _ INTEGER to the
    #end of the file to create a unique file
    from os.path import isfile
    counter = 2
    if isfile(relative_file + EXTENSION):
        relative_file  = relative_file + "_1"
        while isfile(relative_file + EXTENSION):
            relative_file = relative_file[:-1] + str(counter)
            counter += 1

    relative_file = relative_file + EXTENSION

    #Open file for writing
    with open(relative_file, 'w') as f:
        #get relevant features
        name = get_model_type(model)
        params = json.dumps(model.get_params())
        attr = data_to_json(model.__dict__)

        f.write(name + "\n")
        f.write(params)
        f.write(attr)


def load_model(filename):
    """
    Reads a model from a .mlsql file that has already been trained
    @return: the model
    """
    if not file_exists(filename):
        return None

    text = None
    model = None
    with open(filename, 'r') as f:
        model = f.readline()
        text = f.readline()

    dictionary = json.loads(text)

    fit = check_all(model)
    fit.set_params(**dictionary)
    return fit

""""
Helper functions to serialize model into JSON string
Taken from: http://robotfantastic.org/serializing-python-data-to-json-some-edge-cases.html

"""
def isnamedtuple(obj):
    """Heuristic check if an object is a namedtuple."""
    return isinstance(obj, tuple) \
           and hasattr(obj, "_fields") \
           and hasattr(obj, "_asdict") \
           and callable(obj._asdict)

def serialize(data):
    if data is None or isinstance(data, (bool, int, float, str)):
        return data
    if isinstance(data, list):
        return [serialize(val) for val in data]
    if isinstance(data, OrderedDict):
        return {"py/collections.OrderedDict":
                [[serialize(k), serialize(v)] for k, v in data.items()]}
    if isnamedtuple(data):
        return {"py/collections.namedtuple": {
            "type":   type(data).__name__,
            "fields": list(data._fields),
            "values": [serialize(getattr(data, f)) for f in data._fields]}}
    if isinstance(data, dict):
        if all(isinstance(k, str) for k in data):
            return {k: serialize(v) for k, v in data.items()}
        return {"py/dict": [[serialize(k), serialize(v)] for k, v in data.items()]}
    if isinstance(data, tuple):
        return {"py/tuple": [serialize(val) for val in data]}
    if isinstance(data, set):
        return {"py/set": [serialize(val) for val in data]}
    if isinstance(data, np.ndarray):
        return {"py/numpy.ndarray": {
            "values": data.tolist(),
            "dtype":  str(data.dtype)}}
    raise TypeError("Type %s not data-serializable" % type(data))

def restore(dct):
    if "py/dict" in dct:
        return dict(dct["py/dict"])
    if "py/tuple" in dct:
        return tuple(dct["py/tuple"])
    if "py/set" in dct:
        return set(dct["py/set"])
    if "py/collections.namedtuple" in dct:
        data = dct["py/collections.namedtuple"]
        return namedtuple(data["type"], data["fields"])(*data["values"])
    if "py/numpy.ndarray" in dct:
        data = dct["py/numpy.ndarray"]
        return np.array(data["values"], dtype=data["dtype"])
    if "py/collections.OrderedDict" in dct:
        return OrderedDict(dct["py/collections.OrderedDict"])
    return dct

def data_to_json(data):
    return json.dumps(serialize(data))

def json_to_data(s):
    return json.loads(s, object_hook=restore)
