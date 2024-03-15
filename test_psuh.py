# Import necessary libraries
import numpy as np
import pandas as pd  # Ensure pandas is imported
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = pd.read_csv('/home/labsuser/Notebook_into_multi/iris.csv')

X = iris[['sepal_length','sepal_width','petal_length','petal_width']].copy()
y = iris.species

# Add random noise to sepal_width and petal_width only
noise_sepal_width = np.random.uniform(low=0, high=1.0, size=X.shape[0])
noise_petal_width = np.random.uniform(low=0, high=1.0, size=X.shape[0])

X.loc[:, 'sepal_width'] = X['sepal_width'] + noise_sepal_width
X.loc[:, 'petal_width'] = X['petal_width'] + noise_petal_width

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the StandardScaler
scaler = StandardScaler()

# Standardize features
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize the Logistic Regression classifier
log_reg = LogisticRegression(max_iter=1000)

# Train the classifier
log_reg.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = log_reg.predict(X_test_scaled)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)