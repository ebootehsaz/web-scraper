# Import the required libraries
import csv
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

def performSentimentAnalysis():
    # Load the dataset of news headlines from a CSV file
    headlines = []
    labels = []

    with open("news_headlines.csv", newline="") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            headlines.append(row[0])
            labels.append(int(row[1]))
    headlines = np.array(headlines)
    labels = np.array(labels)

    # Create a count vectorizer to extract features from the headlines
    # uses the CountVectorizer to extract features from the headlines. 
    # The fit_transform method analyzes the headlines to identify the 
    # words that are present in the data, and it creates a numerical representation of the data,
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(headlines)

    # Split the data into training and test sets
    n = len(headlines)
    X_train, X_test = X[:n//2], X[n//2:]
    y_train, y_test = labels[:n//2], labels[n//2:]

    # Train a logistic regression model on the training data
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Evaluate the model on the test data
    accuracy = model.score(X_test, y_test)
    print("Accuracy:", accuracy)

    # Use the model to make predictions on new headlines
    new_headlines = ["This news is positive!", "This news is negative!"]
    X_new = vectorizer.transform(new_headlines)
    predictions = model.predict(X_new)
    print("Predictions:", predictions)
