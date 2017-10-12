from ...util.grammar import *
from ...util._constants import choice_columns, column
from pyparsing import CaselessLiteral, Literal, oneOf, Optional, Word, OneOrMore, MatchFirst, Group, delimitedList

def define_replace():
    '''
    Definition of replace keyword
    :returns pyparsing object
    '''
    #define so that there can be multiple verisions of Replace
    replaceKeyword = oneOf(["Replace", "REPLACE"]).setResultsName("replace")

    replace_options = _define_replace_options()

    #putting it all together to create replacement
    replace = replaceKeyword + Optional(replace_options)

    return replace


def _define_replace_options():

    strategyKeyword = (CaselessLiteral('strategy') + Literal('=')).suppress()
    strategyOptions = _strategy_options()
    strategy = strategyKeyword + Quote + MatchFirst(strategyOptions).setResultsName('replaceValue') + Quote

    #missingvals
    missingValKeyword = (CaselessLiteral('missing') + Literal('=')).suppress()
    missingValue = Quote + Word(everythingWOQuotes).setResultsName("replaceIdentifier") + Quote
    missing = missingValKeyword + missingValue

    #persist
    persistKeyword = (CaselessLiteral('persist') + Literal('=')).suppress()
    persistValue = Quote + Word(everythingWOQuotes).setResultsName('replacePersist') + Quote
    persist = Optional(persistKeyword + persistValue)

    option = MatchFirst([strategy, missing, persist])
    replaceOptions = openParen + delimitedList(option, delim=',') + closeParen

    return replaceOptions


def _strategy_options():
    """
    Defines different word replacement strategies for missing values
    - mean, max, min, median, mode
    - drop column
    - drop row
    :returns list of pyparsing object
    """
    mean = CaselessLiteral("mean")
    median = CaselessLiteral("median")
    mode = CaselessLiteral("mode")
    maximum = CaselessLiteral("maximum")
    minimum = CaselessLiteral("minimum")
    dropC = CaselessLiteral("drop column")
    dropR = CaselessLiteral("drop row")

    #Combine all possible options
    options = [mean, median, mode, maximum, minimum, dropC,dropR]

    return options
