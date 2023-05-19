import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the music data from a CSV file
music_data = pd.read_csv('/content/music.csv')

# Prepare the features (X) and target variable (Y)
X = music_data.drop(columns=['genre'])  # Features (all columns except 'genre')
Y = music_data['genre']  # Target variable

# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.8)

# Create a decision tree classifier model
model = DecisionTreeClassifier()

# Train the model using the training data
model.fit(X_train, Y_train)

# Make predictions on the test data
predictions = model.predict(X_test)

# Calculate the accuracy of the model
score = accuracy_score(Y_test, predictions)

# Print the accuracy score
print("Accuracy:", score)
