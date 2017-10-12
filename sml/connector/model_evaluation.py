from .summaries import *
from .util import *

def evaluate_model(keywords, model, algoType, df, X_train, y_train, X_test, y_test, web=False):
    '''
    Metrics phase of SML used to visualize data and results of model
    :keywords - dictionary of keywords and there values
    :model - trained model.
    :algoType - Type of Algorithm used.
    :df - pandas df used
    :X_train - training data (features)
    :y_train - training data (labels)
    :X_test - testing data (features)
    :y_test - testing data (labels)
    '''

    plot_types = []

    from ..python.actions.metrics.visualize import handle_plots

    if model is None:  # Only Lattice Plot available
        if keyword.get('plot_type_values').lower() == 'auto' or keyword.get('plot_type_values').lower() == 'lattice':
            plot_types.append('lattice')

    else:  # More Options available to user with model
        if keywords.get('plot'):#.get('plot_model_type').lower() == 'auto':# and algoType is not None: # Selected AUTO
            if algoType == 'classify':
                plot_types.extend(['lattice','ROC']) # 'learnCurves', 'validationCurves'
            elif algoType == 'regress':
                plot_types.extend(['lattice', 'learnCurves', 'validationCurves'])
            elif algoType == 'cluster':
                plot_types.extend(['lattice', 'learnCurves', 'validationCurves'])

    return handle_plots(plot_types, keywords, algoType, model, df, X_train, y_train, X_test, y_test, web)
