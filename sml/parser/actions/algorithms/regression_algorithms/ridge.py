from pyparsing import oneOf, Literal, Optional, Word
from ....util.grammar import numbers, openParen, closeParen
from ....util._constants import decimal

def define_ridge():
    ridgePhrase = oneOf(["ridge", "Ridge", "RIDGE"])

    #Options
    lambda_phrase = (Literal("lambda") + Literal("=")).suppress()

    lam = Optional(lambda_phrase + decimal.setResultsName("lambda"), default = 0)

    #Compositions
    ridge = ridgePhrase + Optional(openParen + lam + closeParen)

    return ridge
