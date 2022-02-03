from phishing.app import app
import pytest
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


import pytest
import pandas as pd
#import datatest as dt

def mnbdata():
    df= pd.read_csv("PhishingEmail.csv", encoding="latin-1")
    df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
    # Features and Labels
    df['label'] = df['v1'].map({'ham': 0, 'spam': 1})
    df['message']=df['v2']
    df.drop(['v1','v2'],axis=1,inplace=True)
    X = df['message']
    y = df['label']
	
    # Extract Feature With CountVectorizer
    cv = CountVectorizer()
    X = cv.fit_transform(X) # Fit the Data
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    #Naive Bayes Classifier
    from sklearn.naive_bayes import MultinomialNB

    clf = MultinomialNB()
    clf.fit(X_train,y_train)
    pred=clf.predict(X_test)
    clf.score(X_test,y_test)
    acc=acc_score(Y_test, pred)
    print(acc)
    assert acc > 0.65, 'accuracy on test should be > 0.65'


'''
#from sklearn.externals 
import joblib
from sklearn.metrics import r2_score
import numpy as np
def test_prediction_positive_values():
    model = joblib.load('trained_dummy_model.sav')
    X_test = np.array([2, 4, 6, 8, 10, 50]).reshape(-1, 1)
    y_test = np.array([20, 40, 60, 80, 100, 500]).reshape(-1, 1)
    y_preds = model.predict(X_test)
    r2 = r2_score(y_test, y_preds)
    assert r2 == 1
def test_prediction_negative_values():
    model = joblib.load('trained_dummy_model.sav')
    X_test = np.array([-2, -4, -6, -8, -10, -50]).reshape(-1, 1)
    y_test = np.array([-20, -40, -60, -80, -100, -500]).reshape(-1, 1)
    y_preds = model.predict(X_test)
    r2 = r2_score(y_test, y_preds)
    assert r2 == 1




def train_mnb(X, y, test_size=0.33, random_state=42):
    try:
        assert isinstance(X,numpy.ndarray), "X must be a numpy array"
        assert isinstance(Y,numpy.ndarray), "Y must be a numpy array"







@pytest.fixture
def test_preparation():
    test_mnb()
    return split_train_test_data()

@pytest.fixture
def test_mnb(data):
    X_train, X_test, y_train, y_test =train_test_split
    clf= MultinomialNB(X_train,y_train)
    y_pred= predict_on_test_data(clf, x_test)
    return x_test,y_pred
'''