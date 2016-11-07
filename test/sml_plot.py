from sml import execute

query = 'PLOT (modelType="AUTO", plotTypes=[AUTO, AUTO2])'#"AUTO")'
#'READ "data/auto.csv" (separator = "\s+", header = None)'
execute(query, verbose=False)