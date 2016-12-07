import sml
from sml import execute

query = 'READ "data/train.csv" (separator = ",", header = 0) AND\
REPLACE ("NaN", "mode") AND SPLIT (train = .8, test = 0.2) AND\
CLASSIFY (predictors = [1,3,4,5,6,7,8,9,10,11,12], label = 2, algorithm = forest)'
execute(query)
