# SML
SML aims to proved a universal language agnostic framework to simplify the development of machine learning pipelines
____
## Setup
Begin by cloning this repository with the following terminal command
```
git clone https://github.com/UI-DataScience/sml.git
```
Change directories into the main directory and run the following terminal command

```
sudo python3 setup.py develop
```
After running this command, the SML library will be accessible anywhere on your machine via Python.

____
## Simple Code Example

```
import sml
from sml import execute

query1 = 'READ "data/auto.csv" (separator = "\s+", header = None) AND REPLACE ("?", "mode") AND SPLIT (train = .8, test = .2, validation = .0) AND REGRESS (predictors = [2,3,4,5,6,7,8], label = 1, algorithm = simple) AND SAVE "auto.sml"'

execute(query2, verbose=True)

```

With verbose = true, a "pretty" output should be printed out

```
Sml Summary:
=============================================
=============================================
   Dataset:        data/auto.csv
   Delimiter:      \s+
   Training Set Split:       80.00%
   Testing Set Split:        20.00%
   Predictiors:        ['2', '3', '4', '5', '6', '7', '8']
   Label:         1
   Algorithm:     simple
=============================================
=============================================
```
For more extensive documentation on the language, take a look at the [documentation for the parser](https://github.com/UI-DataScience/sml/tree/master/sml/parser)
