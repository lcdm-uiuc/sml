# Getting Started (SML USE-CASES Revisted)
#### Fall 2016

This page contains everything needed to start using SML.

### Contents

- [Introductory Material](https://github.com/UI-DataScience/sml/tree/master/dataflows#introductory-material)
- [Reading in Data](https://github.com/UI-DataScience/sml/tree/master/dataflows#reading-in-data)
- [Seperating Keywords](https://github.com/UI-DataScience/sml/tree/master/dataflows#seperating-keywords)
- [Cleaning Up Data](https://github.com/UI-DataScience/sml/tree/master/dataflows#cleaning-up-data)
- [Partitioning Datasets](https://github.com/UI-DataScience/sml/tree/master/dataflows#partitioning-datasets)
- [Using Classification Alogorithms](https://github.com/UI-DataScience/sml/tree/master/dataflows#using-classification-alogorithms)
- [Using Clustering Algorithms]()
- [Using Regression Algorithms](https://github.com/UI-DataScience/sml/tree/master/dataflows#using-regression-algorithms)
- [Saving / Loading Models](https://github.com/UI-DataScience/sml/tree/master/dataflows#saving--loading-models)
- [Plotting Datasets and Metrics](https://github.com/UI-DataScience/sml/tree/master/dataflows#plotting-datasets-and-metrics-of-algorithms)

___
### Introductory Material

We assumed that you have installed SML, if not please see [Instructions for Installing SML](https://github.com/UI-DataScience/sml#setup) before continuing. For the examples below we use publicly aviliable data which you can download manually nevertheless, for simplicity's sake you can run the following [python script](https://github.com/UI-DataScience/sml/tree/master/dataflows/get_data.py) to obtain the same data and begin running examples. 

___
### Reading in Data
When reading in data using SML one must use the `READ` Keyword followed by the path to the file, for example: 
```python
query = 'READ "/path/to/dataset" '
```

You can also provide optional arguments by including a `()` with arguments for example:
```python
query = 'READ "/path/to/dataset" (sep = ",", header=None) '
```
A list of the all of the READ optional arguments are:
- header - Argument used to specify the header of a dataset. (By default this is None, if no header is present. Otherwise pass in a list or variable names.)
- sep - Argument used to specify what a dataset is delimited by. (For fixed width files, use '\s+')
- dtypes - Argument used to specify the datatype of each column in a dataset.

The table below contains examples of SML reading in Data from various datasets. To view the tutorials using the `READ` command click on the hyperlinks in the Tutorial Column. All of these datasets can be downloaded by clicking the hyperlinks in the Acknowledgment's column. 

Dataset | Task | Acknowledgement | Tutorials
:---: | :---: | :---: | :---:
**Iris** | `READ` | [link](https://archive.ics.uci.edu/ml/datasets/Iris) | [notebook](https://github.com/UI-DataScience/sml/blob/master/dataflows/read/iris-READ.ipynb)
**Auto-MPG** | `READ` | [link](https://archive.ics.uci.edu/ml/datasets/Auto+MPG) | [notebook](https://github.com/UI-DataScience/sml/blob/master/dataflows/read/auto_mpg-READ.ipynb)
**Wine** | `READ`  | [link](https://archive.ics.uci.edu/ml/datasets/Wine) | [notebook](https://github.com/UI-DataScience/sml/blob/master/dataflows/read/wine-READ.ipynb)

___
## Seperating Keywords
When seperating data, we use the keyword `AND` to specify that another action will be performed for the query. As you'll find in subsequent sections you can  combine keywords to form complicated queries. For now consider the following example:

```python
query = 'READ "/path/to/data" (separator = "\s+", header = None) AND\
 REPLACE ("?", "mode") AND SPLIT (train = .8, test = .2, validation = .0) AND\
  REGRESS (predictors = [2,3,4,5,6,7,8], label = 1, algorithm = simple)'
```
While you haven't formally been introducted  to  the  `REPLACE`, `SPLIT`, and `REGRESS` keywords yet, this query will perform the following steps:

- 1. Read the dataset, delimited by "\s+" with no header.
- 2. Next it will replace any values of "?".
- 3. Then it will split the data using a 80/20 split for training and testing respectively.
- 4. Then it will perform regression using columns 2-8 of the dataset as features, and column 1 as the label. The algorithm that SML will use is simple linear regression.

Currently, it's not important to know exactly what every keyword is doing in the query however, it's important to note that each keyword is delimited by an `AND` keyword. In the subsequent sections you'll start to see the `AND` keyword used.
___
## Cleaning Up Data

When working with datasets, values may be missing or *NaNs*, *NAs*, and other troublesome values may be present in a dataset. You can replace these values in SML by using the `REPLACE` keyword. The following example shows the syntax for the `REPLACE` keyword:

```python
'READ "/path/to/data" (separator = ",", header = None) AND REPLACE (missing = "NaN",  strategy = "mode")'
```
When the `REPLACE` keyword is used it requires the first value to be one that you wish to replace, followed by the metric that you want to replace the column with. In the code snippet above you read in some hypotheical dataset and then replace any value of 'NaN' with the mode of the column. Currently the following  metrics have been implemented:
- mode
- mean
- drop column (Removes column if 1 value of the replace value is in a column)
- minimum

Dataset | Task | Acknowledgement | Tutorial
:---: | :---: | :---: | :---:
**Titanic** | `READ` + `REPLACE` |  [link](https://www.kaggle.com/c/titanic/data) |[notebook](https://github.com/UI-DataScience/sml/blob/master/dataflows/replace/Titanic-REPLACE.ipynb)
**Auto-MPG** | `READ` + `REPLACE` | [link](https://archive.ics.uci.edu/ml/datasets/Auto+MPG) | [notebook](https://github.com/UI-DataScience/sml/blob/master/dataflows/replace/autompg-REPLACE.ipynb)

___
## Partitioning Datasets

For almost all situations in Machine Learning it's often useful to split a dataset into Training and Testing sets. To split data with SML you specify the `SPLIT` keyword  The following example shows the SYNTAX for the `SPLIT`: keyword:

```python
query = 'READ "/path/to/data" (separator = ",", header = None) AND SPLIT (train = 0.8, test = 0.2)'
```
The `SPLIT` keyword requires *train* and *test* to have some numerical value that adds up to 1 enclosed in *()*. Here we read some hypthetical dataset using the `READ` keyword. From there we also include the keyword `AND` which specifies that additional command will be used in the query. Then the keyword `SPLIT` is used and we specify that we want 80% of the dataset that is read in to be used for training and the other 20% to be testing. 

The table below contains examples of SML reading in data from various datasets and splitting the data into various training and testing sets. To view the tutorials for the `SPLIT` keyword click on the hyperlinks in the Tutorial Column. All of these datasets can be downloaded by clicking the hyperlinks in the Acknowledgment's column. 


Dataset | Task | Acknowledgement | Tutorial
:---: | :---: | :---: | :---:
**Iris** | `READ` + `SPLIT` | [link](https://archive.ics.uci.edu/ml/datasets/Iris) | [notebook](https://github.com/UI-DataScience/sml/blob/master/dataflows/split/iris-READ-SPLIT.ipynb)
**Auto-MPG** | `READ` + `SPLIT` | [link](https://archive.ics.uci.edu/ml/datasets/Auto+MPG) | [notebook](https://github.com/UI-DataScience/sml/blob/master/dataflows/split/auto_mpg-READ-SPLIT.ipynb)
**Wine** |`READ` + `SPLIT` | [link](https://archive.ics.uci.edu/ml/datasets/Wine) | [notebook](https://github.com/UI-DataScience/sml/blob/master/dataflows/split/wine-READ-SPLIT.ipynb)

___
## Using Classification Alogorithms

If you want to run a classfication algorithm using SML you use the `CLASSIFY` keyword. The current algorithms availiable for classification are:
- Support Vector Machines (SVM) 
- Naive Bayes 
- Random Forest
- Logistic Rergession
- K-Nearest Neighbors

Consider the following code snippet with respect to the syntax for the `CLASSIFY` keyword:
```python
'CLASSIFY (predictors = [1,2,3,4], label = 5, algorithm = svm)'
```
The syntax is to specify `CLASSIFY` with the following enclosed in *()*: columns of the dataset that you want to use as features, the label you want to classify, and the algorithm that you want to use.

The table below contains examples of SML reading in data from various datasets, splitting the data into various training and testing sets, and performing classifcation over the dataset with a classifcation algorithim. To view the tutorials for the `CLASSIFY` keyword click on the hyperlinks in the Tutorial Column. All of these datasets can be downloaded by clicking the hyperlinks in the Acknowledgment's column. 

*It's worth noting that for the Titanic, Chronic Kidney Disease, and U.S Census Dataset the REPLACE keyword is used, this keyword will be talked about in a subsequent section.*


Dataset | Task | Algorithm | Acknowledgement | Tutorial
:---: | :---: | :---: | :---: | :---:
**Iris** | `READ` + `SPLIT` + `CLASSIFY` | SVM | [link](https://archive.ics.uci.edu/ml/datasets/Iris) | [notebook](https://github.com/UI-DataScience/sml/blob/master/dataflows/classify/iris_SVM-READ-SPLIT-CLASSIFY.ipynb)
**Spam Detection** | `READ` + `SPLIT` + `CLASSIFY` | Naive Bayes | [link](https://archive.ics.uci.edu/ml/datasets/Spambase) |[notebook](https://github.com/UI-DataScience/sml/blob/master/dataflows/classify/spam_NaiveBayes-READ-SPLIT-CLASSIFY.ipynb)
**Titanic** | `READ` +  `REPLACE` + `SPLIT` + `CLASSIFY` | Random Forest |[link](https://www.kaggle.com/c/titanic/data) |[notebook](https://github.com/UI-DataScience/sml/blob/master/dataflows/classify/Titanic_RandomForest-READ-SPLIT-CLASSIFY.ipynb)
**Chronic Kidney Disease** | `READ` + `REPLACE` + `SPLIT` + `CLASSIFY`  | Logistic Regression | [link](https://archive.ics.uci.edu/ml/datasets/Chronic_Kidney_Disease) | [notebook](https://github.com/UI-DataScience/sml/blob/master/dataflows/classify/Kidney-Logistic_Regression-READ-SPLIT-REPLACE-CLASSIFY.ipynb)
**U.S. Census** | `READ` + `REPLACE` + `SPLIT` + `CLASSIFY` | Logistic Regression | [link](https://archive.ics.uci.edu/ml/datasets/US+Census+Data+%281990%29) | [notebook](https://github.com/UI-DataScience/sml/blob/master/dataflows/classify/Census-READ-SPLIT-REPLACE-CLASSIFY.ipynb)

___
## Using Clustering Algorithms (Tutorials Still Under Construction)
If you want to run clustering algorithms using SML you use the `CLUSTER` keyword. The current algorithms availiable for clustering are: 
- K-Means Clustering

Consider the following code snippet with respect to the syntax for the `CLUSTER` keyword:
```python
'CLUSTER (predictors = [1,2,3,4,5,6,7], algorithm = kmeans)'
```
The syntax is to specify `CLUSTER` with the following enclosed in *()*: columns of the dataset that you want to use as features, and the algorithm that you want to use.

The table below contains examples of SML reading in data from various datasets, splitting the data into various training and testing sets, and performing clustering over the dataset with a clustering algorithim. To view the tutorials for the `CLUSTER` keyword click on the hyperlinks in the Tutorial Column. All of these datasets can be downloaded by clicking the hyperlinks in the Acknowledgment’s column.

Dataset | Task | Algorithm | Acknowledgement | Tutorial
:---: | :---: | :---: | :---: | :---:
**Seeds** | `READ` + `SPLIT` + `CLUSTER` | K-Means | [link](https://archive.ics.uci.edu/ml/datasets/seeds) | notebook
**Wine** | `READ` + `SPLIT` + `CLUSTER` | ? | [link](https://archive.ics.uci.edu/ml/datasets/Wine) | notebook
___
## Using Regression Algorithms
If you want to run regression algorithms using SML you use the `REGRESS` keyword. The current algorithms availiable for regression are:

- Simple Linear Regression
- Ridge Regression
- Lasso Regression
- Elastic Net Regression

Consider the following code snippet with respect to the syntax for the `REGRESS` keyword:
```python
'REGRESS (predictors = [1,2,3,4,5,6,7,8,9], label = 10, algorithm = ridge)'
```
The syntax is to specify `REGRESS`  with the following enclosed in (): columns of the dataset that you want to use as features, the label that you want to predict and the algorithm that you want to use to do regression.

The table below contains examples of SML reading in data from various datasets, splitting the data into various training and testing sets, and performing regression over the dataset with a specific regression algorithim. To view the tutorials for the `REGRESS` keyword click on the hyperlinks in the Tutorial Column. All of these datasets can be downloaded by clicking the hyperlinks in the Acknowledgment’s column.

Dataset | Task | Algorithm | Acknowledgement | Tutorial
:---: | :---: | :---: | :---: | :---:
**Auto-MPG** | `READ` + `REPLACE` + `SPLIT` + `REGRESS` | Simple Linear Regression | [link](https://archive.ics.uci.edu/ml/datasets/Auto+MPG) | [notebook](https://github.com/UI-DataScience/sml/blob/master/dataflows/regress/autompg_LinearRegression-READ-REPLACE-SPLIT-REGRESS.ipynb)
**Computer Hardware** | `READ` + `SPLIT` + `REGRESS` | Ridge Regression | [link](https://archive.ics.uci.edu/ml/datasets/Computer+Hardware) | [notebook](https://github.com/UI-DataScience/sml/blob/master/dataflows/regress/computer-RidgeRegression-READ-SPLIT-REGRESS.ipynb)
**Boston Housing** | `READ` + `SPLIT` + `REGRESS` | Elastic Net | [link](https://archive.ics.uci.edu/ml/datasets/Housing) | [notebook](https://github.com/UI-DataScience/sml/blob/master/dataflows/regress/BostonHousing_ElasticNet-READ-SPLIT-REGRESS.ipynb)
___

## Saving / Loading Models
### (Working on LOAD in dataflow...)

It's possible to save models and reuse them later. To save a model in SML you use the `SAVE` keyword.
Consider the following code snippet with respect to the syntax for the `SAVE` keyword:
```python
'SAVE "path/to/save/model"'
```

The syntax is to specify `SAVE` followed by the path to save the model enclosed in `""`.

To use this model again you use the `LOAD` keyword. Consider the following code snippet with respect to the syntax for the `LOAD` keyword:
```python
'LOAD /path/to/load/model'
```

The syntax is to specify `LOAD`  followed by the path to save the model.

The table below contains an example of SML reading in data from various datasets, splitting the data into various training and testing sets, and performing regression over the Auto-MPG dataset with a simple linear regression. The model is saved and then reloaded. To view the tutorials for the `SAVE` & `LOAD` keywords click on the hyperlink in the Tutorial Column.  Again you can download the Auto-MPG dataset by clicking on the hyperlink in the Acknowledgement Column.

Dataset | Task | Algorithm | Acknowledgement | Tutorial
:---: | :---: | :---: | :---: | :---:
**Auto-MPG** | `READ` + `REPLACE` + `SPLIT` + `REGRESS` + `SAVE` + `LOAD` | Simple Linear Regression | [link](https://archive.ics.uci.edu/ml/datasets/Auto+MPG) | [notebook](https://github.com/UI-DataScience/sml/blob/master/dataflows/regress/autompg_LinearRegression-READ-REPLACE-SPLIT-REGRESS.ipynb)



___
## Plotting Datasets and Metrics of Algorithms

When using SML it's possible to plot datasets or metrics of algorithms. The syntax to do this is `PLOT` followed by the enclosing the following in *()* The model type and the plot types. Consider the following code snippet with respect to the syntax for the `PLOT` keyword:
```python
'PLOT (modelType="AUTO", plotTypes="AUTO")''
```
Here were telling SML to generate plots based on the modelType (Regression, Classifcation, Clustering) that would provide the best information about the model and dataset.

The table below contains examples of SML reading in data from various datasets, splitting the data into various training and testing sets, and performing some machine learning task over the dataset with a specific algorithim. To view the tutorials for the `PLOT` keyword click on the hyperlinks in the Tutorial Column. All of these datasets can be downloaded by clicking the hyperlinks in the Acknowledgment’s column.

Dataset | Task | Algorithm | Acknowledgement | Tutorial
--- | --- | --- | --- | ---
**Iris** | `READ` + `SPLIT` + `CLASSIFY` + `PLOT` | SVM | [link](https://archive.ics.uci.edu/ml/datasets/Iris) | [notebook](https://github.com/UI-DataScience/sml/blob/master/dataflows/plot/iris_svm-READ-SPLIT-CLASSIFY-PLOT.ipynb)
**Auto-MPG** | `READ` + `SPLIT` + `REGRESS` + `PLOT`| Simple Linear Regression | [link](https://archive.ics.uci.edu/ml/datasets/Auto+MPG) | [notebook](https://github.com/UI-DataScience/sml/blob/master/dataflows/plot/autompg_linear_regression-READ-SPLIT-REGRESS-PLOT.ipynb)
**Seeds** | `READ` + `SPLIT` + `CLUSTER` + `PLOT`| K-Means | [link](https://archive.ics.uci.edu/ml/datasets/seeds) | [notebook](https://github.com/UI-DataScience/sml/blob/master/dataflows/plot/seeds-READ-SPLIT-CLUSTER-PLOT.ipynb)
