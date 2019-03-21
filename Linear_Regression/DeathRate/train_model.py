import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import ensemble
from sklearn.metrics import mean_absolute_error
from sklearn.externals import joblib

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

# Remove prediction column data from the feature data
del features_df['2016']

# Create the X and y arrays
X = features_df.to_numpy()
y = df['2016'].to_numpy()

# Split the data set in a training set (70%) and a test set (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Using default GradientBoostingRegressor with verbose 1 to see output
model_1 = ensemble.GradientBoostingRegressor(
    verbose=1
)

print("Training the model 1 using the GradientBoosting Regressor")
model_1.fit(X_train, y_train)

# Save the trained model to a file so we can use it in other programs
joblib.dump(model_1, 'processed/trained_death_rate_classifier_model_1.pkl')

# Find the error rate on the training set using the best parameters
train_mae = mean_absolute_error(y_train, model_1.predict(X_train))
print("Training Set Mean Absolute Error: %.3f" % train_mae)

# Find the error rate on the test set using the best parameters
test_mae = mean_absolute_error(y_test, model_1.predict(X_test))
print("Test Set Mean Absolute Error: %.3f" % test_mae)
