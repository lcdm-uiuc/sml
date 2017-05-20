from .actions.actions_list import define_actionList
from pyparsing import restOfLine, MatchFirst
from .util._constants import *
from .util.grammar import *


def smlparser():
"""
Define SML Parser.
:returns Legal set of actions as a pyparsing object
"""
    comment = _define_comment()
    actionList = define_actionList()
    return actionList

def _define_comment(comment="--"):
"""
Define Comments for Parser.

:comment -- Option Arg Accepts String of Characters.
:returns expression that will be used as a comment
"""

    oracleSqlComment = comment + restOfLine
    return oracleSqlComment
