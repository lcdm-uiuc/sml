from ...util.grammar import *
from ...util._constants import index_and_type_list

from pyparsing import Word, Keyword, Optional, MatchFirst, Literal, oneOf, delimitedList

def define_read():
    filename = Word(everythingWOQuotes).setResultsName("filename")
    #define so that there can be multiple verisions of READ
    readKeyword = Keyword("read", caseless = True).setResultsName("read")
    #Compose Read Optionals
    readOptions = _define_read_options()
    read = readKeyword + Quote + filename + Quote + Optional(readOptions)
    return read

def _define_read_options():
    #header
    Nones = oneOf('None')
    headerLiteral = (Literal("header") + Literal("=")).suppress()
    header_choices = MatchFirst([Word(numbers), bool_true, bool_false, Nones]).setResultsName("header")
    header = headerLiteral + header_choices

    #separator
    separatorLiteral = (Literal("separator") + Literal("=")).suppress()
    definesep = Quote + Word(everythingWOQuotes + whitespace).setResultsName("sep") + Quote
    separator = separatorLiteral + definesep

    #datatypes
    dtypesPhrase = (Literal("types") + Literal("=")).suppress()
    dtypesDef = index_and_type_list.setResultsName("dtypes")
    dtypes = dtypesPhrase + openBracket + dtypesDef + closeBracket

    option = MatchFirst([header, dtypes, separator])
    readOptions = openParen + delimitedList(option, delim=',') + closeParen
    return readOptions
