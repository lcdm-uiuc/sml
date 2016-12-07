import sml
from sml import execute

query = 'READ "data/iris.csv" AND \
 SPLIT (train = .8, test = 0.2) AND \
 CLASSIFY (predictors = [1,2,3,4], label = 5, algorithm = svm) and SAVE "iris.sml"'

execute(query)
