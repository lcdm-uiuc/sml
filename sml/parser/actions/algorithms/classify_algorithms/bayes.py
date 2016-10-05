"""
Defines the parsing for the naive algorithm for intended use in classification
"""
from pyparsing import oneOf, Literal, Optional, Word
from ....util.grammar import numbers, openParen, closeParen
from ....util._constants import decimal

def define_bayes():
    bayesPhrase = oneOf(["bayes", "Bayes", "BAYES"])

    #Compositions
    bayes = bayesPhrase + Optional(openParen + closeParen)

    return(bayes)
