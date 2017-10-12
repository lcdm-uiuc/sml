from pyparsing import *
from ..util.grammar import *
from ..util._constants import index_and_type_list
from ..util._constants import choice_columns, column


def define_apply():
    applyKeyword = Keyword("apply", caseless = True).setResultsName("apply")
    fileName = Word(everythingWOQuotes).setResultsName("applyFileName")
    options = _define_apply_options()
    ret = applyKeyword + Quote + fileName + Quote + Optional(options)
    return ret

def _define_apply_options():
    '''
    Definition of Optional Arguments for APPLY Keyword
    :returns pyparsing object
    '''
    #header
    Nones = oneOf('None')
    headerLiteral = (Literal("header") + Literal("=")).suppress()
    header_choices = MatchFirst([Word(numbers), bool_true, bool_false, Nones]).setResultsName("applyHeader")
    header = headerLiteral + header_choices

    #separator
    separatorLiteral = (Literal("separator") + Literal("=")).suppress()
    definesep = Quote + Word(everythingWOQuotes + whitespace).setResultsName("applySep") + Quote
    separator = separatorLiteral + definesep

    #datatypes
    dtypesPhrase = (Literal("types") + Literal("=")).suppress()
    dtypesDef = index_and_type_list.setResultsName("applyDTypes")
    dtypes = dtypesPhrase + openBracket + dtypesDef + closeBracket

    #Phrases to organize predictor and label column numbers
    predPhrase = (Literal("predictors") + Literal("=")).suppress()
    labelPhrase = (Literal("label") + Literal("=")).suppress()

    #define predictor and label column numbers
    predictorsDef = choice_columns.setResultsName("applyPredictors")
    labelDef = column.setResultsName("applyLabel")

    #combine phrases with found column numbers
    preds = predPhrase + predictorsDef
    labels = labelPhrase + labelDef


    option = MatchFirst([header, dtypes, separator, preds, labels])
    applyOptions = openParen + delimitedList(option, delim=',') + closeParen
    return applyOptions
