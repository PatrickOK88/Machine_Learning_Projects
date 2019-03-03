import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import ensemble
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import GridSearchCV

# Load the data set
df = pd.read_csv("processed/endangered_species.csv")

# Remove the fields from the data set that we don't want to include in our model
del df['id_no,N,10,0']
del df['compiler,C,200']
del df['citation,C,254']
del df['source,C,254']
del df['dist_comm,C,254']
del df['island,C,200']
del df['subspecies,C,50']
del df['subpop,C,200']
del df['tax_comm,C,250']

# convert column data to 1/0 values
df["marine,C,5"] = df["marine,C,5"].map({'t': 1, 'f': 0})
df["terrestial,C,5"] = df["terrestial,C,5"].map({'t': 1, 'f': 0})
df["freshwater,C,5"] = df["freshwater,C,5"].map({'t': 1, 'f': 0})

# convert output data to values 0, 1, 2 etc
df["category,C,5"] = df["category,C,5"].map({'EX': 1,
                                             'EW': 2,
                                             'CR': 3,
                                             'EN': 4,
                                             'VU': 5,
                                             'NT': 6,
                                             'LC': 7,
                                             'DD': 8})

# Replace categorical data with one-hot encoded data
features_df = pd.get_dummies(df, columns=['binomial,C,254',
                                          'legend,C,80',
                                          'kingdom,C,100',
                                          'phylum,C,100',
                                          'class,C,100',
                                          'order_,C,100',
                                          'family,C,100',
                                          'genus,C,100'])

# Remove category from the feature data
del features_df['category,C,5']

# Create the X and y arrays
X = features_df.to_numpy()
y = df['category,C,5'].to_numpy()

# Split the data set in a training set (70%) and a test set (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Create the model
model = ensemble.GradientBoostingRegressor()

# Gradient Boosting Classifier
param_grid = {
    'n_estimators': [1500, 2000],
    'learning_rate': [0.06, 0.1, 0.3],
    'max_depth': [6, 8],
    'min_samples_leaf': [3, 6],
    'max_features': [0.8, 1.0],
    'loss': ['ls'],
    'random_state': [0],
    'verbose': [1]
}

# 'learning_rate': 0.1, 'loss': 'ls', 'max_depth': 6, 'max_features': 1.0, 'min_samples_leaf': 3,
# 'n_estimators': 1500, 'random_state': 0, 'verbose': 1
#
# Training Set Mean Absolute Error: 0.3095
# Test Set Mean Absolute Error: 0.4301

# Define the grid search.
gs_cv = GridSearchCV(model, param_grid, cv=3, n_jobs=-1, verbose=5)

# Run the grid search - on only the training data
gs_cv.fit(X_train, y_train)

# Print the parameters that gave us the best result
print(gs_cv.best_params_)

# Find the error rate on the training set using the best parameters
train_mae = mean_absolute_error(y_train, gs_cv.predict(X_train))
print("Training Set Mean Absolute Error: %.4f" % train_mae)

# Find the error rate on the test set using the best parameters
test_mae = mean_absolute_error(y_test, gs_cv.predict(X_test))
print("Test Set Mean Absolute Error: %.4f" % test_mae)
