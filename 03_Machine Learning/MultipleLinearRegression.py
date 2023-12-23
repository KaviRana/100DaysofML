# THOERY
"""Multiple linear regression is a statistical method that uses several independent variables to predict a dependent variable.
The goal of multiple linear regression is to find a linear relationship between the independent variables and the dependent variable.
The equation for multiple linear regression is: y = b0 + b1x1 + b2x2 + ... + bnxn
where:

y is the dependent variable
b0 is the intercept
b1, b2, ..., bn are the coefficients for the independent variables
x1, x2, ..., xn are the independent variables
The coefficients for the independent variables are found using a process called least squares. Least squares is a method for finding the values of the coefficients that minimize the sum of the squared errors.

Multiple linear regression can be used to solve a variety of problems. For example, it can be used to:

Predict the price of a house based on its size, number of bedrooms, and location
Predict the sales of a product based on its price, advertising, and distribution
Predict the risk of a patient developing a disease based on their age, sex, and medical history
Multiple linear regression is a powerful tool that can be used to make predictions about a variety of phenomena. However, it is important to remember that multiple linear regression is only a model. It is not a perfect representation of reality. As such, it is important to interpret the results of multiple linear regression with caution.
"""


class MeraLR:

    def __init__(self):
        self.coef_ = None
        self.intercept_ = None

    def fit(self, X_train, y_train):
        X_train = np.insert(X_train, 0, 1, axis=1)

        # calcuate the coeffs
        betas = np.linalg.inv(np.dot(X_train.T, X_train)).dot(X_train.T).dot(y_train)
        self.intercept_ = betas[0]
        self.coef_ = betas[1:]

    def predict(self, X_test):
        y_pred = np.dot(X_test, self.coef_) + self.intercept_
        return y_pred