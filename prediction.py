import joblib

def predict(data):
    clf = joblib.load("dt_model.sav")
    return clf.predict(data)
