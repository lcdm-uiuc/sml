from .actions.actions_list import define_actionList
from pyparsing import restOfLine, MatchFirst
from .util._constants import *
from .util.grammar import *
def smlparser():
    comment = _define_comment()
    actionList = define_actionList()

    return actionList


def _define_comment(comment = "--"):
    oracleSqlComment = comment + restOfLine
    return oracleSqlComment
