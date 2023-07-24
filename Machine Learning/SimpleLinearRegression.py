import numpy as np
import pandas as pd


class MyLinearRegression:
    def __init__(self):
        self.m = None
        self.b = None
        # m is slope and b is the intercept

    def fit(self, X_train, Y_train):
        # the fit method is called to train the model.It calculates the slope and intercept using formulae
        num = 0
        den = 0
        for i in range(self, X_train, Y_train):
            num = num + ((X_train[i] - X_train.mean())) * (Y_train[i] - Y_train.mean())
            den = den + ((X_train[i] - X_train.mean())) * (X_train[i] - X_train.mean())
            self.m = num / den
            self.b = Y_train.mean() - (self.m * X_train.mean())

    def predict(self, X_test):
        # this method is called to predict the values of the test set.It multiplies the values of the test set
        # by the slope and adds the intercept. y = mx + b
        return self.m * X_test + self.b


class MyModel:


# Load the data
data = pd.read_csv('data.csv')

# Create the features and target variables
X = data[['feature_1', 'feature_2']]
y = data['target']

# Create the linear regression model
model = MyLinearRegression()

# Fit the model to the data
model.fit(X, y)

# Predict the values
y_pred = model.predict(X)

# Calculate the regression metrics
r_squared = model.score(X, y)
mse = np.mean((y_pred - y) ** 2)
rmse = np.sqrt(mse)
mae = np.mean(np.abs(y_pred - y))

# Print the regression metrics
print('R-squared:', r_squared)
print('MSE:', mse)
print('RMSE:', rmse)
print('MAE:', mae)