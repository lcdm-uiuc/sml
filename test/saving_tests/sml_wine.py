import sml
from sml import execute

query = 'READ "data/wine.csv" (separator = ";", header = 0) AND SPLIT (train = .8, test = 0.2) AND CLASSIFY (predictors = [1,2,3,4,5,6,7,8,9,10,11], label = 12, algorithm = knn) and SAVE "wine.sml"'

execute(query)
