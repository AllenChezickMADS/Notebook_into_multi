'''
This file completes a logistic regression for regular and noised iris data
'''
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.datasets import load_iris

def do_regular_iris():
    '''
    Input: None 
    Action: loads iris data and completes testing
    Output: returns model score
    '''
    iris = pd.read_csv('/home/labsuser/Notebook_into_multi/iris.csv')
    X = iris[['sepal_length','sepal_width','petal_length','petal_width']].copy()
    y = iris.species

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
    return accuracy 

def split_data(data):
    '''
    Input: Noised dataframe   
    Action: completes testing for noised data, gets no_noised results
    Output: print statement of both model scores
    '''
    X = data[['sepal_length','sepal_width','petal_length','petal_width']].copy()
    y = data.species
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
    get_regular = do_regular_iris()
    print(f"Accuracy for regular model {get_regular} VS Accuracy for noised model {accuracy}" )
     