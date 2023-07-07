from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply data scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define the individual classifiers
classifier1 = LogisticRegression(max_iter=1000)
classifier2 = KNeighborsClassifier()
classifier3 = DecisionTreeClassifier()

# Define the voting classifier using different voting mechanisms
majority = VotingClassifier(estimators=[('lr', classifier1), ('knn', classifier2), ('dt', classifier3)], voting='hard')
weighted = VotingClassifier(estimators=[('lr', classifier1), ('knn', classifier2), ('dt', classifier3)], voting='soft', weights=[2, 1, 1])
soft = VotingClassifier(estimators=[('lr', classifier1), ('knn', classifier2), ('dt', classifier3)], voting='soft')

# Train the voting classifiers
majority.fit(X_train_scaled, y_train)
weighted.fit(X_train_scaled, y_train)
soft.fit(X_train_scaled, y_train)

# Make predictions using the voting classifiers
y_pred_majority = majority.predict(X_test_scaled)
y_pred_weighted = weighted.predict(X_test_scaled)
y_pred_soft = soft.predict(X_test_scaled)

# Calculate and print the accuracy scores
accuracy_majority = accuracy_score(y_test, y_pred_majority)
accuracy_weighted = accuracy_score(y_test, y_pred_weighted)
accuracy_soft = accuracy_score(y_test, y_pred_soft)

print("Accuracy (Majority Voting): {:.2f}".format(accuracy_majority))
print("Accuracy (Weighted Voting): {:.2f}".format(accuracy_weighted))
print("Accuracy (Soft Voting): {:.2f}".format(accuracy_soft))
