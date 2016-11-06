from sml import execute

query = 'READ "data/iris.csv" AND \
         SPLIT (train = .8, test = 0.2)'
execute(query, verbose=True)