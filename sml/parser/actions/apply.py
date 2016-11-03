from pyparsing import *
from ..util.grammar import *

def define_apply():
    applyKeyword = Keyword("apply", caseless = True).setResultsName("apply")
    fileName = Word(everythingWOQuotes).setResultsName("applyFileName")
    options = _define_apply_options()
    ret = applyKeyword + Quote + fileName + Quote
    return ret

def _define_apply_options():
    return None
