from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

 Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Perform bootstrap sampling on the training data
bootstrap_indices = np.random.choice(len(X_train), size=len(X_train), replace=True)
X_train_bootstrapped = X_train[bootstrap_indices]
y_train_bootstrapped = y_train[bootstrap_indices]

base_estimator = DecisionTreeClassifier()
bagging = BaggingClassifier(estimator=base_estimator, n_estimators=10, random_state=42)
bagging.fit(X_train_bootstrapped, y_train_bootstrapped)
y_pred = bagging.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
