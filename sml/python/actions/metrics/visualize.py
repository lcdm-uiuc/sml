import matplotlib.pyplot as plt
import seaborn as sns

def handle_plots(plot_types, keywords, algoType, model, df, X_train, y_train, X_test, y_test):

	for plot_type in plot_types:
		if plot_type == 'lattice':
			plot_lattice(df, keywords)
		if plot_type == 'ROC':
			plot_ROC(algoType, model, keywords, df, X_test, y_test)
		if plot_type == 'learnCurves':
			learnCurves(model, X_train, y_train) 
		if plot_type == 'validationCurves':
			validationCurves(model, X_test, y_test)


def plot_lattice(df, keywords):
	
	columns = list(df.columns.values)  #  TODO:Change this later to selected columns in grammer, for now just do all...
	fig, ax = plt.subplots(len(columns), len(columns))
	# TODO Map all colors
	# TODO Add Option For color
	# TODO Add Option to get label
	# Default is to select colors for now
	for col1, i in enumerate(columns):
		for col2, j in enumerate(columns):
			if i == j:
				sns.kdeplot(df[df.columns[col1]], ax=ax[col1][col2], shade=True, legend=False)
			else:
				sns.kdeplot( df[df.columns[col1]], df[df.columns[col2]], ax=ax[col1][col2])

			# Formatting
			ax[i,j].set_xticklabels([])
			ax[i,j].set_yticklabels([])
			ax[i,j].set_ylabel('')
			ax[i,j].set_xlabel('')

			
			# TODO: if they specify headers set x and y labels
			#if j == 0:
			#	ax[i,j].set_xticklabels([])
			#	ax[i,j].set_ylabel(column_headers[i])
			#	ax[i,j].set_ylabel('')
			#	ax[i,j].set_xlabel('')
			#if i == len(columns)-1:
			#	ax[i,j].set_xlabel('')
			#	ax[i,j].set_xlabel(column_headers[j])
			#elif i == len(columns)-1:
			#	ax[i,j].tick_params(axis='y', which='major', bottom='off')
			#	ax[i,j].set_yticklabels([])
			#	ax[i,j].set_xlabel(column_headers[j])
			#	ax[i,j].set_ylabel('')
			#else:
			#	ax[i,j].set_xticklabels([])
			#	ax[i,j].set_xlabel('')
			#	ax[i,j].set_yticklabels([])
			#	ax[i,j].set_ylabel('')

	# TODO: Add Option to Save Figure
	plt.show()
	plt.close()


def plot_ROC(algoType, model, keywords, df, X_test, y_test):
	from sklearn.preprocessing import label_binarize
	from sklearn.metrics import roc_curve, auc
	import sklearn.cross_validation as cv
	import numpy as np
	#print (df)
	fpr = dict()
	tpr = dict()
	roc_auc = dict()


	# Must Binarize Data
	_classes = y_test.unique().tolist()
	labels = label_binarize(y_test, classes=_classes)
	n_classes = labels.shape[1]

	X_test_bin, _ = cv.train_test_split(np.c_[X_test.values], test_size=0) # Binarize data
	y_test_bin, _ = cv.train_test_split(labels, test_size=0) # Binarize data

	predict_score = model.decision_function(X_test_bin)

	# Generates ROC Curve
	for i in range(n_classes):
		fpr[i], tpr[i], _ = roc_curve(y_test_bin[:, 1], predict_score[:, i])
		roc_auc[i] = auc(fpr[i], tpr[i])
	
	# Plotting ROC Curve
	line_width = 3  # TO DO: User can change line_width
	for i in range(n_classes):
		plt.plot(fpr[i], tpr[i], lw=line_width, label='ROC curve of class of {0} (Area = {1:0.2f})'.format(_classes[i], roc_auc[i]))

	# TODO: They can specify y limit, x limit, x label, y label legend (location)

	plt.plot([0, 1], [0, 1], 'k--', lw=line_width)
	plt.xlim([0, 1.0])
	plt.ylim([0.0, 1.025])
	plt.xlabel('False Positive Rate')
	plt.ylabel('True Positive Rate')

	#TODO: Can specify to save pic (dpi as well)

	plt.legend(loc="lower right")
	#plt.savefig('iris_roc.png', dpi=300)
	plt.show()
	plt.close()

def learnCurves(model, X_train, y_train):
	from sklearn.learning_curve import learning_curve
	import numpy as np

	# Generating Learning Curve
	train_sizes, train_scores, test_scores = learning_curve(model, X_train, y_train) 
	
	# Plotting Learning Curve
	plt.figure()

	# TODO: User specifies labels
	plt.xlabel("Training examples")
	plt.ylabel("Score")

	train_scores_mean = np.mean(train_scores, axis=1)
	train_scores_std = np.std(train_scores, axis=1)
	test_scores_mean = np.mean(test_scores, axis=1)
	test_scores_std = np.std(test_scores, axis=1)

	plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
	                 train_scores_mean + train_scores_std, alpha=0.1,
	                 color="orange")
	plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
	                 test_scores_mean + test_scores_std, alpha=0.1, color="purple")
	plt.plot(train_sizes, train_scores_mean, 'o-', color="orange",
	         label="Training score")
	plt.plot(train_sizes, test_scores_mean, 'o-', color="purple",
	         label="Cross-validation score")

	# TODO: User adds legend
	plt.legend(loc="best")

	#TODO User can save fig

	plt.show()
	plt.close()

def validationCurves(model, X_test, y_test):
	from sklearn.learning_curve import validation_curve
	import numpy as np

	param_range = np.arange(0, 5)

	# Generating Validation Curve
	sucess=False
	for params in model.get_params().keys():  # KI: Doesn't seem to have an effect on validation curve will look into further
		try:
			v_train_scores, v_test_scores = validation_curve(model, X_test, y_test, param_name=params, param_range=param_range)
			sucess = True
		except:
			pass
		if sucess: break

	plt.figure()
	plt.xlabel("Validation examples")
	plt.ylabel("Score")

	v_train_scores_mean = np.mean(v_train_scores, axis=1)
	v_train_scores_std = np.std(v_train_scores, axis=1)
	v_test_scores_mean = np.mean(v_test_scores, axis=1)
	v_test_scores_std = np.std(v_test_scores, axis=1)

	plt.fill_between(param_range, v_train_scores_mean - v_train_scores_std,
	                 v_train_scores_mean + v_train_scores_std, alpha=0.1,
	                 color="orange")
	plt.fill_between(param_range, v_test_scores_mean - v_test_scores_std,
	                 v_test_scores_mean + v_test_scores_std, alpha=0.1, color="purple")

	plt.plot(param_range, v_train_scores_mean, 'o-', color="orange",
	         label="Training score")

	plt.plot(param_range, v_test_scores_mean, 'o-', color="purple",
	         label="Cross-validation score")

	plt.legend(loc="best")
	plt.show()
	plt.close()
	