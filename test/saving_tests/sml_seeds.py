import sml
from sml import execute

query = 'READ "data/seeds.csv" (separator = "\s+", header = 0) AND SPLIT (train = .8, test = .2, validation = .0) AND CLUSTER (predictors = [1,2,3,4,5,6,7], algorithm = kmeans) and SAVE "seeds.sml"'

execute(query, verbose=True)
