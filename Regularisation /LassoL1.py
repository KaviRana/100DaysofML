#The code starts by generating a synthetic regression dataset using make_regression. 
#Next, it applies PolynomialFeatures to create polynomial features and fits the models 
#(linear regression without Lasso and Lasso regression) to the transformed data. Then, it plots the original data points 
#and the fitted curves for both models. The resulting plot demonstrates the distinction in the fitted curves, 
#emphasizing how Lasso regularization effectively controls overfitting by shrinking coefficients and promoting sparsity in the model.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.datasets import make_regression

# Generate a synthetic regression dataset with polynomial features
X, y = make_regression(n_samples=100, n_features=1, noise=20)
poly = PolynomialFeatures(degree=10)
X_poly = poly.fit_transform(X)

# Initialize and fit models
withoutL1 = LinearRegression()
withL1 = Lasso(alpha=0.1)
withoutL1.fit(X_poly, y)
withL1.fit(X_poly, y)

plt.scatter(X, y, color='red', label='Original Data')

# Predict and plot the fitted curves from withoutL1
X_plot = np.linspace(np.min(X), np.max(X), 100).reshape(-1, 1)
X_plot_poly = poly.transform(X_plot)
y_withoutL1 = withoutL1.predict(X_plot_poly)
plt.plot(X_plot, y_withoutL1, color='blue', linewidth=2, label='Polynomial Regression (without L1)')

# Predict and plot the fitted curves from withL1
y_withL1 = withL1.predict(X_plot_poly)
plt.plot(X_plot, y_withL1, color='green', linewidth=2, label='Polynomial Regression (with L1)')

# Set plot labels and legend
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.title('Comparison of Polynomial Regression with and without L1 Regularization')
plt.grid(True)
plt.show()
