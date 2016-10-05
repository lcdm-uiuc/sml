import sml
from sml import execute

query1 = 'READ "data/census.csv" (separator=",", header = 0, types = [1:numeric, 2:string]) AND REPLACE ("NaN", "mode") and SPLIT (train = .8, test = 0.2) and CLASSIFY (predictors=[1,2,3,4,5 , 6,7, 8, 9, 10 ,11 ,12, 13,14], label = 15, algorithm = logistic)'


execute(query1, verbose=False)
