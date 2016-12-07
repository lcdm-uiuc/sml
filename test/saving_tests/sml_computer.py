import sml
from sml import execute

query = 'READ "data/computer.csv" (separator = ",", header = 0) AND \
SPLIT (train = .8, test = .2, validation = .0) AND \
REGRESS (predictors = [1,2,3,4,5,6,7,8,9], label = 10, algorithm = ridge) and SAVE "computer.sml"'

execute(query, verbose=True)
