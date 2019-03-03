# Endangered Species Prediction

### Disclaimer
This was made for recreational use and should by no means used as a means to prove the outcome of endangered species.
Please refer to the [website](https://www.iucnredlist.org/) for data on endangered species

### Overview
The objective of this project is predicting the IUCN: Red List category an animal will have as defined in the IUCN: Red List of Threatened Species.\
- __Extinct (EX__ 				- no remaining individuals of the species.
- __Extinct in the wild (EW)__ 	- Captive individuals survive, but there is no free-living, natural population.
- __Critically endangered (CR)__ 	- Faces an extremely high risk of extinction in the immediate future.
- __Endangered (EN)__ 			- Faces a high risk of extinction in the near future.
- __Vulnerable (VU)__ 			- Faces a high risk of endangerment in the medium term.
- __Near-threatened (NT)__ 		- May be considered threatened in the near future.
- __Least concern (LC)__ 			- No immediate threat to species' survival.

### Downloads
For this project we will be using the spatial data provided on the IUCN: Red List [website](https://www.iucnredlist.org/resources/spatial-data-download)\
__Note:__ 
- You will have to set up an account in order to download the data.
- I downloaded MAMMALS, AMPHIBIANS and MARINEFISH data

### Installation instructions
- The requiremnets for running this project can be found in requirements.txt\
- Install the requirements listed in requirements.txt using pip install -r\
- This was made using the PyCharm IDE which can be downloaded for free [here](https://www.jetbrains.com/pycharm/download/#section=windows)\
- Anaconda was also used and it can be downloadedvfor free [here](https://www.anaconda.com/download/)\
- Git bash was used for commands outlined below in "Setup instructions" & "Usage Instructions"


### Setup instructions
1. Clone the repo
2. Go into the project folder\
 *cd Endangered_Species*
3. Create a directory called __data__\
 *mkdir data*
4. Copy the downloaded data to the newly created directory __data__\
 *cp <path to dir><downloaded_data.zip> data/*
5. Go into the __data__ folder\
 *cd data*
6. Unzip the downloaded data\
 *tar -xvf <downloaded_data.zip>*
7. Delete unwanted zip file\
 *rm * .zip*
8. Delete all data apart from the .dbf files and keep just the dbf files\
 *find . -type f ! -name "&ast;.dbf" -exec rm {} \\;*
9. Go back to __loan-prediction__ folder\
 *cd ../*
10. Create a folder for our output\
 *mkdir processed*

__Note:__ I used opened the files in excel and converted them to .csv files for use in this project

### Usage instructions
Go into the project folder\
*cd Endangered_Species*

#### Run __python create_data.py__
- This file will prepare the data in a .csv file that will be used to train the model.
- Headers in the data will be explicitly defined to avoid descrepencies
- Combines all the into one single .csv file called *endangered_species.csv* into the precessed directory
- Note: This can take quite some time to complete depending on amount of data used.

#### Run __python view_data.py__
- This file creates a html file of the first 100 rows in the endangered_species.csv file so data can be esily viewed

#### Run __python train _model.py__
- This file uses the data in the __endangered_species.csv__ file to train the model
- Removes the fields from the data set that wasn't deemed inmportant to include in the model as I felt these features had no impact on the end result
- Convertes coulnms with strings to 0/1 values
- Convertes the prediction categories into numerical values
- Replaces columns with one-hot encoding
- Split the data set in a training set (70%) and a test set (30%)
- Sets the weights for the model
- Saves the trained model to a file so we can use it in other programs
- Outputs the prediction error/mean absolute error of the test data and the train data
	
#### Run __feature_selection.py__
- Used to test the trained model.
- Open the file an input the header values.
- It should predict the coreect category for the input data



### Troubleshooting
If for some reason packages aren't installed in Anaconda you can use the following command in Anaconda Prompt:\
*conda install [package_name]*\
If you run into issues with incompatable packages you can first update the package using\
*conda update [package_name]*\
or do a fresh reinstall of the package with\
*conda uninstall [package_name]*
*conda install [package_name]*

