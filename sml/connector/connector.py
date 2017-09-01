"""
Processes input after it has been parsed. Performs the dataflow for input.
"""
from .model_building import build_model
from .model_application import apply_model
from .model_evaluation import evaluate_model
from .summaries import *
from .util import *


def handle(parsing, verbose):

    '''
    :parsing - Parsed pyparsing object
    :verbose - boolean variable used to control type of messaged displayed to console
    Main Function that handles model phase, apply phase, and metric phase of SML
    '''

    keywords = keyword_check(parsing)
    # print(keywords)

    model, df, X_train, y_train, X_test, y_test, algoType = build_model(keywords, verbose)

    if model is not None:  # If model isn't created no need to run through apply phase
        result = apply_model(keywords, model, X_test, y_test)
        return result
    elif model is None:
        print("no model")


    if keywords.get('plot'):  # for now plot is the only thing that needs to be specified
        evaluate_model(keywords, model, algoType, df, X_train, y_train, X_test, y_test)
