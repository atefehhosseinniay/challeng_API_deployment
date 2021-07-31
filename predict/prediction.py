import joblib

#import pickle

model = joblib.load(open(r'C:\Users\atefe\Desktop\challenge_api\model\model_GB.pkl','rb'))
def predict(dataset):
    prediction = model.predict(dataset)
    return prediction

