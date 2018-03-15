#Handle Missing Data - Imputer
#Label Encoding      - OneHotEncoding
#Feature Scaling     - StandardScaler
#Train Test Split    - train_test_split

from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,OneHotEncoder

from sklearn.linear_model import LinearRegression

import pandas as pd
import numpy as np

dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

#print(X)

# Imputer - Handle Missing Data
imputer = Imputer(missing_values='NaN', strategy='mean')
X[:,1:3] = imputer.fit_transform(X[:,1:3])

#print(X)

# Label Encoding
label = LabelEncoder()
X[:,0] = label.fit_transform(X[:,0])
print(X)

oneHot = OneHotEncoder(categorical_features=[0])
X = oneHot.fit_transform(X).toarray()
print(X)


# Feature Scaling
sc = StandardScaler()
X[:,3:5] = sc.fit_transform(X[:,3:5])

# Train Test Split
X_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2)




