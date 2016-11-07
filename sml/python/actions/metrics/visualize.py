import matplotlib.pyplot as plt
import seaborn as sns

def handle_plots(plot_types, keywords, model, df, X_train, y_train, X_test, y_test):
	for plot_type in plot_types:
		if plot_type == 'lattice':
			plot_lattice(df, keywords)
		if plot_type == 'ROC':
			plot_ROC(model, X_test, y_test)
		if plot_type == 'learnCurves':
			learnCurves(X_train, y_train)
		if plot_type == 'validationCurves':
			validationCurves(X_test, y_test)


def plot_lattice(df, keywords):
	# Check keywords for column names....
	columns = list(df.columns.values)  # Change this later to selected columns, for now just do all...
	single_colors = None
	colormaps = None

	pass

def plot_ROC(model, X_test, y_test):
	pass

def learnCurves(X_train, y_train):
	pass

def validationCurves(X_test, y_test):
	pass