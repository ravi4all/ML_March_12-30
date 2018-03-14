#Handle Missing Data - Imputer
#Label Encoding      - OneHotEncoding
#Feature Scaling     - StandardScaler
#Train Test Split    - train_test_split

from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

from sklearn.linear_model import LinearRegression

import pandas as pd
import numpy as np

dataset = pd.read_csv('Social_Network_Ads.csv')
