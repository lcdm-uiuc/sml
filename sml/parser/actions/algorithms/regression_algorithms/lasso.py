from pyparsing import oneOf, Literal, Optional, Word
from ....util.grammar import numbers, openParen, closeParen
from ....util._constants import decimal

def define_lasso():
    lassoPhrase = oneOf(["lasso", "Lasso", "LASSO"])

    #Options
    lambda_phrase = (Literal("lambda") + Literal("=")).suppress()

    lam = Optional(lambda_phrase + decimal.setResultsName("lambda"), default = 0)

    #Compositions
    lasso = lassoPhrase + Optional(openParen + lam + closeParen)

    return lasso
