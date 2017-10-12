from pyparsing import oneOf, Literal, Word, Optional, Combine, delimitedList, MatchFirst, CaselessLiteral
from ...util.grammar import *


def define_encode():
    encodeKeyword = CaselessLiteral("encode").setResultsName('encode')
    encode_options = _define_encode_options()
    encode = encodeKeyword + Optional(encode_options)
    return encode

def _define_encode_options():
    #encode strategy
    strategyKeyword = (CaselessLiteral('strategy') + Literal('=')).suppress()
    strategyOptions = _define_encode_strategies()
    strategy = strategyKeyword + Quote + MatchFirst(strategyOptions).setResultsName('encodeStrategy') + Quote

    #persist
    persistKeyword = (CaselessLiteral('persist') + Literal('=')).suppress()
    persistValue = Quote + Word(everythingWOQuotes).setResultsName('encodePersist') + Quote
    persist = Optional(persistKeyword + persistValue)

    option = MatchFirst([strategy, persist])
    encodeOptions = openParen + delimitedList(option, delim=',') + closeParen

    return encodeOptions

def _define_encode_strategies():
    one_hot = CaselessLiteral("one-hot")
    regular = CaselessLiteral("regular")

    return [regular, one_hot]
