# Preprocessing Keywords
## READ
Reads from a csv file.

### Structure
READ "< FileName >" (separator = < separator>, header = < header >, dtypes = [< column name > : < dtype >])

### Example
```
'READ "data/census.csv" (separator=",", header = 0, types = [1:numeric, 2:string])
```
The command above reads the file
"census.csv" with comma delimiter, the zeroth column as the header and specifying types for column 1 to be numeric and column 2 to be string
___

## REPLACE
Performs imputation on missing values
### Structure
REPLACE ("< Missing Value >", "< Imputation Strategy >")

### Example
```
REPLACE ("NaN", "mode")
```
The command above replaces NaN missing values with the mode of that column
___

## SPLIT
___
### Structure
SPLIT (train = < train >, test = < test >)

### Example
```
SPLIT (train = .8, test = .2)
```

The command above splits the data into 80% training and 20% validation
___
