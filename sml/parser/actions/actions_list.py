from .algorithms.classify import define_classify
from .algorithms.regress import define_regress
from .algorithms.cluster import define_cluster
from .preprocessing.read import define_read
from .preprocessing.split import define_split
from .preprocessing.replace import define_replace
from .preprocessing.encode import define_encode
from .apply import define_apply

from .IO.load import define_load
from .IO.save import define_save

from .visualize.plot import define_plot

from ..util.grammar import *
from ..util._constants import *
from pyparsing import *

def define_actionList():
    '''
    :returns list of defined actions in sml which can be delimited by AND
    '''

    action = _define_action()
    actionList = delimitedList(action, delim = AND)
    return actionList

def _define_action():
    '''
    :returns list action XORed
    '''

    classify = define_classify()
    regress = define_regress()
    cluster = define_cluster()
    read = define_read()
    split = define_split()
    replace = define_replace()
    load = define_load()
    save = define_save()
    applyAction = define_apply()
    plot = define_plot()
    encode = define_encode()

    action = classify ^ regress ^cluster ^ read ^split^ replace ^ load ^ save ^ plot ^ applyAction ^ encode

    return action
