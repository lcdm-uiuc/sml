import sml
from sml import execute

query1 = 'READ "data/auto.csv" (separator = "\s+", header = None) AND REPLACE (missing = "?", strategy = "mode") AND SPLIT (train = .8, test = .2, validation = .0) AND REGRESS (predictors = [2,3,4,5,6,7,8], label = 1, algorithm = lasso) AND SAVE "auto.sml"'


execute(query1, verbose=True)
