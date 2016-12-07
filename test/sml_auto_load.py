import sml
from sml import execute

query1 = 'LOAD auto.sml AND\
  REGRESS (predictors = [2,3,4,5,6,7,8], label = 1, algorithm = simple)'

execute(query1, verbose=True)
