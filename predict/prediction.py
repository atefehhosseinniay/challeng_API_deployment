import joblib

#import pickle

model= joblib.load('model_GB.pkl')

def predict(dataset):
    prediction = model.predict(dataset)
    return prediction

