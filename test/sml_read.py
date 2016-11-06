from sml import execute

query = 'READ "data/auto.csv" (separator = "\s+", header = None)'
execute(query, verbose=False)


query = 'READ "data/auto.csv" (separator = "\s+", header = None)'
execute(query, verbose=True)

#TODO: Fix header Bug
#query = 'READ "data/auto.csv" (separator = "\s+", header = [test1,test2,test3,test4,test5,test6,test6,test7,test8,test9])'
#execute(query, verbose=True)
