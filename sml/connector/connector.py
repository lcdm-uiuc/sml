"""
Processes input after it has been parsed. Performs the dataflow for input.
"""
import numpy as np

from .summaries import *
from .util import *
from .model_building import build_model
from .model_application import apply_model
from .model_evaluation import evaluate_model
from .data_processing import process_data

def handle(parsing, verbose, web=False):

    '''
    :parsing - Parsed pyparsing object
    :verbose - boolean variable used to control type of messaged displayed to console
    Main Function that handles model phase, apply phase, and metric phase of SML
    '''
    keywords = keyword_check(parsing)

    df, data_train, data_test = process_data(keywords,verbose)
    model, algoType, summary_msg = build_model(keywords, data_train ,verbose)

    if df is None and model is None:
        print("Please either READ in data or select a Model to build")
        return None


    if model is not None:  # If model isn't created no need to run through apply phase
        apply_result = apply_model(keywords, model, data_test)
        return apply_result
    else:
        apply_result = None

    if keywords.get('plot'):  # for now plot is the only thing that needs to be specified
        metric_result = evaluate_model(keywords, model, algoType, df, X_train, y_train, X_test, y_test, web)
    else:
        metric_result = None

    if web:
        return {'model_summary': summary_msg, 'apply_summary': apply_result, 'metric_summary': metric_result}
