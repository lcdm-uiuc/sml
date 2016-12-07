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
    from os.path import isfile,splitext
    counter = 2
    if isfile(relative_file + EXTENSION):
        relative_file  = relative_file + "_1"
        while isfile(relative_file + EXTENSION):
            relative_file = relative_file[:-1] + str(counter)
            counter += 1
    if EXTENSION in relative_file:
        relative_file = relative_file.replace(EXTENSION, '')
    relative_file = relative_file + EXTENSION

    #Open file for writing
    with open(relative_file, 'w') as f:
        #get relevant features
        name = get_model_type(model)
        params = json.dumps(model.get_params(deep=True))
        f.write(name + "\n")
        f.write(params + '\n')


def load_model(filename):
    """
    Reads a model from a .sml file that has already been trained
    @return: the model
    """
    if not file_exists(filename):
        print('File ' + filename + ' not found')
        return None

    text = None
    model = None
    with open(filename, 'r') as f:
        model = f.readline()
        paramText = f.readline()
        attrText = f.readline()


    params = json.loads(paramText)

    fit = check_all(model)
    fit.set_params(**params)
    return fit
