"""
Defines all parser functionality for the CLUSTER keyword
"""
from ...util.grammar import *
from ...util._constants import choice_columns
from .cluster_algorithms import kmeans
from pyparsing import Literal, oneOf, Optional, Word, Keyword, MatchFirst, delimitedList, CaselessLiteral

def define_cluster():
    '''
    Algorithm Definition of Cluster Keyword
    :returns pyparsing object
    '''

    algoPhrase = (Literal ("algorithm") + Literal("=")).suppress()

    kmeansd = kmeans.define_kmeans()
    algo = algoPhrase + MatchFirst([kmeansd]).setResultsName("algorithm")

    # Grammar for Feature Selection
    feature_prefix = Optional(CaselessLiteral("feature") + Literal("=")).suppress()
    feature_value = oneOf(["False", "AUTO", "RFE"]).setResultsName("feature")
    feature = feature_prefix + feature_value

    #define so that there can be multiple verisions of Cluster
    clusterKeyword = Keyword("cluster", caseless=True).setResultsName("cluster")

    #define predictor word to specify column numbers
    predPhrase = (Literal("predictors") + Literal("=")).suppress()
    predictorsDef = choice_columns.setResultsName("predictors")
    preds = predPhrase + predictorsDef
    labelPhrase = (Literal("label") + Literal("=")).suppress()
    labelDef = choice_columns.setResultsName("label")
    labels = labelPhrase + labelDef

    option = MatchFirst([preds, labels, algo])
    options = delimitedList(option, delim=',')

    cluster = clusterKeyword + openParen + Optional(options)+ closeParen

    return cluster
