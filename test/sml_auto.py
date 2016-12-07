import sml
from sml import execute

<<<<<<< HEAD:test/sml_auto.py
query1 = 'READ "data/auto.csv" (separator = "\s+", header = None) AND REPLACE (missing = "?", strategy = "mode") AND SPLIT (train = .8, test = .2, validation = .0) AND REGRESS (predictors = [2,3,4,5,6,7,8], label = 1, algorithm = lasso)'
=======
query1 = 'READ "data/auto.csv" (separator = "\s+", header = None) AND REPLACE (missing = "?", strategy = "mode") AND SPLIT (train = .8, test = .2, validation = .0) AND REGRESS (predictors = [2,3,4,5,6,7,8], label = 1, algorithm = simple) AND SAVE "auto"'
>>>>>>> a603c8c12439512720b992160fe3ccad53063096:test/sml_auto.py


execute(query1, verbose=True)
