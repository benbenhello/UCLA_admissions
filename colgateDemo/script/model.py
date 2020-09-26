import pandas as pd
import numpy as np
import sys
## data preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

## regression model
from sklearn.ensemble import RandomForestRegressor

def random_forest(train_X, train_y, test_X):
    model = RandomForestRegressor(n_estimators = 100, random_state = 42)
    model.fit(train_X, train_y)
    predict = model.predict(test_X)
    train_predict = model.predict(train_X)
    print(predict)

def benben(gre = 316.47, toelf = 107.19, university = 3, sop = 3.37, lor = 3.48, cgpa = 8.58, research = 0):
    
  	return np.array([[gre,toelf,university,sop,lor,cgpa,research]])

raw_data = pd.read_csv("/Users/ben/Desktop/UCLA_admissions/colgateDemo/script/Admission_Predict_Ver1.1.csv")
raw_data.set_index('Serial No.', inplace=True)
raw_data.index.name = "No"
raw_data = raw_data.rename(columns = {'Chance of Admit ': 'Chance', \
                                      'GRE Score': 'GRE', \
                                      'TOEFL Score': 'TOEFL', \
                                      'University Rating': 'Rating', \
                                     })
# print(raw_data.head())
Y = raw_data["Chance"].values
X = raw_data.drop(["Chance"],axis=1)
scaler_X = MinMaxScaler(feature_range = (0, 1))
scale_X = scaler_X.fit_transform(X.copy())
input_gre = 316.47 if sys.argv[1] == '-1' else sys.argv[1]
input_toefl = 107.19 if sys.argv[2] == '-1' else sys.argv[2]
input_university = 3 if sys.argv[3] == '-1' else sys.argv[3]
input_sop = 3.37 if sys.argv[4] == '-1' else sys.argv[4]
input_lor = 3.48 if sys.argv[5] == '-1' else sys.argv[5]
input_cgpa = 8.58 if sys.argv[6] == '-1' else sys.argv[6]
input_research = 0 if sys.argv[7] == '-1' else sys.argv[7]
test_X = benben(input_gre,input_toefl,input_university,input_sop,input_lor,input_cgpa,input_research)
test_scale_X = scaler_X.transform(test_X.copy())
random_forest(scale_X, Y, test_scale_X)

















