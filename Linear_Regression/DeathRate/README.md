# Death Rate Prediction

### Disclaimer
This was made for recreational use and should by no means used as a means to prove the outcome of endangered species.
Please refer to the [website](https://data.worldbank.org/indicator/SP.DYN.CDRT.IN?end=2016&start=1960&view=chart) for data on world Death Rates

### Overview
The objective of this project is predicting the Death Rate per 1,000 people in the world
A file for Jupyter Notebook will also be provided. I suggest using this as it will be done step by step and it will be easier to follow. 

### Downloads
For this project we will be using the spatial data provided on the [website](https://data.worldbank.org/indicator/SP.DYN.CDRT.IN?end=2016&start=1960&view=chart)


### Installation instructions
- The requirements for running this project can be found in requirements.txt\
- Install the requirements listed in requirements.txt using pip install -r\
- This was made using the PyCharm IDE which can be downloaded for free [here](https://www.jetbrains.com/pycharm/download/#section=windows)\
- Anaconda was also used and it can be downloaded for free [here](https://www.anaconda.com/download/)\
- Git bash was used for commands outlined below in "Setup instructions" & "Usage Instructions"


### Setup instructions
1. Clone the repo

### Usage instructions
Go into the project folder\
*cd DeathRate*

#### Run __python train_model.py__
- This file uses the data in the __DeathRate.csv__ file to train the model
- Removes the fields from the data set that wasn't deemed important to include in the model as I felt these features had no impact on the end result
- Replaces columns with one-hot encoding
- Split the data set in a training set (70%) and a test set (30%)
- Sets the weights for the model
- Saves the trained model to a file so we can use it in other programs
- Outputs the prediction error/mean absolute error of the test data and the train data
	
#### Run __python grid_search.py__
- Works exactly like train_model.py except it does a grid search using multiple values for each parameter in order to get the "best" parameter options

#### Using Linear Regression - Death Rate.ipynb
 - You will require Jupyter Notebook to run this file
 - Does a step by step guide of the GradientBoostingRegressor plotting graphs for multiple values for each parameter
 - Analyses the graphs in order to determine the best values for the model.


### Troubleshooting
If for some reason packages aren't installed in Anaconda you can use the following command in Anaconda Prompt:\
*conda install [package_name]*\
If you run into issues with incompatible packages you can first update the package using\
*conda update [package_name]*\
or do a fresh reinstall of the package with\
*conda uninstall [package_name]*
*conda install [package_name]*

