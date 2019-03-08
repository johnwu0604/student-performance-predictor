import pandas as pd
from joblib import dump, load

''' Predictor class for outputting model result '''
class Predictor:

    def __init__(self, verbose=True):
        # store list of columns
        self.columns = ['school','sex','age','address','famsize','Pstatus','Medu','Fedu','traveltime','studytime','failures','schoolsup',
            'famsup','paid','activities','higher','internet','romantic','famrel','freetime','goout','Dalc','Walc','health','absences']
        # load the trained model
        self.model = load('model/model.joblib') 

    ''' Preprocess feature data '''
    def preprocess(self, features):
        features['school'].replace(['GP','MS'],[0,1],inplace=True)
        features['sex'].replace(['F','M'],[0,1],inplace=True)
        features['address'].replace(['U','R'],[0,1],inplace=True)
        features['famsize'].replace(['LE3','GT3'],[0,1],inplace=True)
        features['Pstatus'].replace(['T','A'],[0,1],inplace=True)
        features['schoolsup'].replace(['no','yes'],[0,1],inplace=True)
        features['famsup'].replace(['no','yes'],[0,1],inplace=True)
        features['paid'].replace(['no','yes'],[0,1],inplace=True)
        features['activities'].replace(['no','yes'],[0,1],inplace=True)
        features['higher'].replace(['no','yes'],[0,1],inplace=True)
        features['internet'].replace(['no','yes'],[0,1],inplace=True)
        features['romantic'].replace(['no','yes'],[0,1],inplace=True)
        return features

    ''' Read data from a post request '''
    def read_data(self, request):
        data = []
        data.append(request.form['school'])
        data.append(request.form['sex'])
        data.append(request.form['age'])
        data.append(request.form['address'])
        data.append(request.form['famsize'])
        data.append(request.form['Pstatus'])
        data.append(request.form['Medu'])
        data.append(request.form['Fedu'])
        data.append(request.form['traveltime'])
        data.append(request.form['studytime'])
        data.append(request.form['failures'])
        data.append(request.form['schoolsup'])
        data.append(request.form['famsup'])
        data.append(request.form['paid'])
        data.append(request.form['activities'])
        data.append(request.form['higher'])
        data.append(request.form['internet'])
        data.append(request.form['romantic'])
        data.append(request.form['famrel'])
        data.append(request.form['freetime'])
        data.append(request.form['goout'])
        data.append(request.form['Dalc'])
        data.append(request.form['Walc'])
        data.append(request.form['health'])
        data.append(request.form['absences'])

        features = pd.DataFrame([data],columns=self.columns)
        return features

    ''' Make a prediction given a set of features '''
    def predict(self, request):
        features = self.read_data(request)
        processed = self.preprocess(features)
        prediction = self.model.predict(processed)
        return prediction
        