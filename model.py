# Importing the libraries
import numpy as np
import pandas as pd
import pickle

data = pd.read_csv('score.csv')

x = data.drop(columns=['Name','Grade'])
y = data['Grade']

# Import label encoder 
from sklearn import preprocessing 
  
label_encoder = preprocessing.LabelEncoder() 
  
# Encode labels in column 'Grade'
y = label_encoder.fit_transform(y) 

from sklearn.ensemble import RandomForestClassifier
regressor = RandomForestClassifier()

#Fitting model with trainig data
regressor.fit(x, y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[12, 45, 32, 34, 21]]))