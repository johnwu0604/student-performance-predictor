from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from joblib import dump, load
import pandas as pd

# load dataset
data = pd.read_csv('student_data.csv')

# preprocess data
data['passed'].replace(['no','yes'],[0,1],inplace=True)
data['school'].replace(['GP','MS'],[0,1],inplace=True)
data['sex'].replace(['F','M'],[0,1],inplace=True)
data['address'].replace(['U','R'],[0,1],inplace=True)
data['famsize'].replace(['LE3','GT3'],[0,1],inplace=True)
data['Pstatus'].replace(['T','A'],[0,1],inplace=True)
data['schoolsup'].replace(['no','yes'],[0,1],inplace=True)
data['famsup'].replace(['no','yes'],[0,1],inplace=True)
data['paid'].replace(['no','yes'],[0,1],inplace=True)
data['activities'].replace(['no','yes'],[0,1],inplace=True)
data['higher'].replace(['no','yes'],[0,1],inplace=True)
data['internet'].replace(['no','yes'],[0,1],inplace=True)
data['romantic'].replace(['no','yes'],[0,1],inplace=True)

# seprate data into feature and targets
features = data.drop(['passed'], axis=1)
labels = data[['passed']]

# split into 80% train and 20% test
x_train, x_test, y_train, y_test = train_test_split(
    features, labels, test_size=0.2, random_state=42, shuffle=True)

# train model
model = GaussianNB()
model.fit(x_train, y_train.values.ravel())

# save model 
dump(model, 'model.joblib') 

# score results
y_pred = model.predict(x_test)
f1_score = f1_score(y_test, y_pred)

print(f1_score) 


