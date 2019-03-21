import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import ensemble
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import GridSearchCV

# Load the data set
df = pd.read_csv("processed/Death_Rate.csv")
print(df.shape)

missing_val = [col for col in df.columns if df[col].isnull().any()]
print(missing_val)

for val in missing_val:
    df[val] = df[val].fillna(df[val].mean())

# Remove the fields from the data set that we don't want to include in our model
del df['Country Code']
del df['Indicator Name']
del df['Indicator Code']

# Replace categorical data with one-hot encoded data
features_df = pd.get_dummies(df, columns=['Country Name'])

# Remove category from the feature data
del features_df['2016']

# Create the X and y arrays
X = features_df.to_numpy()
y = df['2016'].to_numpy()

# Split the data set in a training set (70%) and a test set (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Create the model
model = ensemble.GradientBoostingRegressor()

param_grid = {
    'learning_rate': [1, 0.6, 0.3, 0.1, 0.06, 0.03, 0.01],
    'n_estimators': [1, 2, 4, 8, 16, 32, 64, 128],
    'min_samples_split': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    'min_samples_leaf': [1, 3, 5, 10, 20],
    'max_depth': [1, 3, 5, 10, 20],
    'max_features': ['auto', 'sqrt', 0.2],
    'verbose': [1]
}

# Define the grid search.
gs_cv = GridSearchCV(model, param_grid, cv=3, n_jobs=-1, verbose=5)

# Run the grid search - on only the training data
gs_cv.fit(X_train, y_train)

# Print the parameters that gave us the best result
print(gs_cv.best_params_)

# Find the error rate on the training set using the best parameters
train_mae = mean_absolute_error(y_train, gs_cv.predict(X_train))
print("Training Set Mean Absolute Error: %.3f" % train_mae)

# Find the error rate on the test set using the best parameters
test_mae = mean_absolute_error(y_test, gs_cv.predict(X_test))
print("Test Set Mean Absolute Error: %.3f" % test_mae)
