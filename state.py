import pandas as pd
from joblib import dump, load

''' State Tracker class for keeping track of current states in the frontend '''
class StateTracker:

    def __init__(self, verbose=True):
        # set the initial states
        self.state = {
            'school' : 'GP', 
            'sex': 'F',
            'age': 18,
            'address': 'U',
            'famsize': 'GT3',
            'Pstatus': 'A',
            'Medu': 4,
            'Fedu': 4,
            'traveltime': 2,
            'studytime': 2,
            'failures': 0,
            'schoolsup': 'yes',
            'famsup': 'no',
            'paid': 'no',
            'activities': 'no',
            'higher': 'yes',
            'internet': 'no',
            'romantic': 'no',
            'famrel': 4,
            'freetime': 3,
            'goout': 4,
            'Dalc': 1,
            'Walc': 1,
            'health': 3,
            'absences': 10,
            'result': ''
        }

    ''' Updates the current state '''
    def updateState(self, request):
        self.state['school'] = request.form['school']
        self.state['sex'] = request.form['sex']
        self.state['age'] = request.form['age']
        self.state['address'] = request.form['address']
        self.state['famsize'] = request.form['famsize']
        self.state['Pstatus'] = request.form['Pstatus']
        self.state['Medu'] = request.form['Medu']
        self.state['Fedu'] = request.form['Fedu']
        self.state['traveltime'] = request.form['traveltime']
        self.state['studytime'] = request.form['studytime']
        self.state['failures'] = request.form['failures']
        self.state['schoolsup'] = request.form['schoolsup']
        self.state['famsup'] = request.form['famsup']
        self.state['paid'] = request.form['paid']
        self.state['activities'] = request.form['activities']
        self.state['higher'] = request.form['higher']
        self.state['internet'] = request.form['internet']
        self.state['romantic'] = request.form['romantic']
        self.state['famrel'] = request.form['famrel']
        self.state['freetime'] = request.form['freetime']
        self.state['goout'] = request.form['goout']
        self.state['Dalc'] = request.form['Dalc']
        self.state['Walc'] = request.form['Walc']
        self.state['health'] = request.form['health']
        self.state['absences'] = request.form['absences']
        