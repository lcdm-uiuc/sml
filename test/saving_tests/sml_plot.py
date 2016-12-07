from sml import execute

# Trying Classify
print ('Classifying')
query = 'READ "data/iris.csv" AND \
 SPLIT (train = .8, test = 0.2) AND \
 CLASSIFY (predictors = [1,2,3,4], label = 5, algorithm = svm) AND \
 PLOT (modelType="AUTO", plotTypes="AUTO")'

execute(query)

# Trying Regression
print ('Regressing')
query = 'READ "data/auto.csv" (separator = "\s+", header = None) AND REPLACE (missing = "?", strategy = "mode") AND SPLIT (train = .8, test = .2, validation = .0) AND \
REGRESS (predictors = [2,3,4,5,6,7,8], label = 1, algorithm = simple) AND PLOT (modelType="AUTO", plotTypes="AUTO")'

execute(query, verbose=False)

# Trying Clustering