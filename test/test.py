from sml.parser.parser import smlparser
from sml.sml import execute
query1 = 'READ "data/auto.csv" (separator = "\s+", header = None) AND\
 REPLACE ("?", "mode") AND SPLIT (train = .8, test = .2, validation = .0) \
 AND REGRESS (predictors = [2,3,4,5,6,7,8], label = 1, algorithm = simple)'
query2 = 'READ "data/boston.csv" (separator = "\s+", header = 0) AND \
SPLIT (train = .8, test = .2, validation = .0) \
AND REGRESS (predictors = [1,2,3,4,5,6,7,8,9,10,11,12,13], \
label = 14, algorithm = elastic)'
query3 = 'READ "data/census.csv" (separator=",", header = 0, types = [1:numeric,2:string])\
 AND REPLACE ("NaN", "mode") AND SPLIT (train = .8, test = 0.2) \
 AND CLASSIFY (predictors=[1,2,3,4,5,6,7,8,9,10,11,12,13,14], label = 15, \
 algorithm = logistic)'
query4 = 'READ "data/chronic.csv" (separator = ",", header = None) AND \
REPLACE ("?", "mode") AND SPLIT (train = .8, test = 0.2) AND CLASSIFY \
(predictors = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],\
 label = 25, algorithm = logistic)'
query5 = 'READ "data/computer.csv" (separator = ",", header = 0) AND \
SPLIT (train = .8, test = .2, validation = .0) \
AND REGRESS (predictors = [1,2,3,4,5,6,7,8,9], label = 10, algorithm = ridge)'
query6 = 'READ "data/iris.csv" AND SPLIT (train = .8, test = 0.2) AND \
CLASSIFY (predictors = [1,2,3,4], label = 5, algorithm = svm)'
query7 = 'READ "data/seeds.csv" (separator = "\s+", header = 0) AND \
SPLIT (train = .8, test = .2, validation = .0) AND \
CLUSTER (predictors = [1,2,3,4,5,6,7], algorithm = kmeans)'
query8 = 'READ "data/spam.csv" AND SPLIT (train = .8, test = 0.2) AND \
CLASSIFY (predictors = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,\
20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,\
46,47,48,49,50,51,52,53,54,55,56], label = 58, algorithm = bayes)'
query9 = 'READ "data/train.csv" (separator = ",", header = 0) AND \
REPLACE ("NaN", "mode") AND SPLIT (train = .8, test = 0.2) AND \
CLASSIFY (predictors = [1,3,4,5,6,7,8,9,10,11,12], label = 2, algorithm = forest)'
query10 = 'READ "data/wine.csv" (separator = ";", header = 0) AND \
SPLIT (train = .8, test = 0.2) AND CLASSIFY (predictors = [1,2,3,4,5,6,7,8,9,\
10,11], label = 12, algorithm = knn)'

queries = [query1,query2,query3,query4,query5,query6,query7,query8,query9,\
            query10]

x = smlparser()
count = 0
for query in queries:
    try:
        execute(query)
    except:
        print("query " + str(count + 1) + " failed")
    count = count + 1
