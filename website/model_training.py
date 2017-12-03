import datetime
import numpy as np
import pandas as pd
from sklearn import model_selection
from keras.layers import Input, Dense
from keras.models import Model
from sklearn import preprocessing
from sklearn import neighbors as knn

data = pd.read_csv("extendedData.csv").dropna()
data.reset_index(drop=True, inplace=True)
data = data.drop('Unnamed: 0', 1)
data = data.drop('address', 1)
data = data.drop('id', 1)
data = data.drop('name', 1)
data = data.drop('collection_id', 1)

for j, k in enumerate(data["DOB"]):
    data.at[j, "DOB"] = datetime.datetime.now().year - int(data.at[j, "DOB"][:4])
data.rename(columns={'DOB' : 'age'}, inplace=True)

le_city = preprocessing.LabelEncoder()
le_city.fit(data['city'])
data['city'] = le_city.transform(data['city'])
le_sex = preprocessing.LabelEncoder()
le_sex.fit(data['sex'])
data['sex'] = le_sex.transform(data['sex'])
le_state = preprocessing.LabelEncoder()
le_state.fit(data['state'])
data['state'] = le_state.transform(data['state'])
le_marital_status = preprocessing.LabelEncoder()
le_marital_status.fit(data['MARITAL_STATUS'])
data['MARITAL_STATUS'] = le_marital_status.transform(data['MARITAL_STATUS'])
le_tobacco = preprocessing.LabelEncoder()
le_tobacco.fit(data['TOBACCO'])
data['TOBACCO'] = le_tobacco.transform(data['TOBACCO'])
le_purchased = preprocessing.LabelEncoder()
data['PURCHASED'] = ["None" if type(i)==float else i for i in list(data["PURCHASED"])]
le_purchased.fit(data['PURCHASED'])
data['PURCHASED'] = le_purchased.transform(data['PURCHASED'])

data = data.apply(pd.to_numeric, errors='ignore')
# TODO: Predict Bronze and diff(bronze, silver)

model = knn.NearestNeighbors(n_neighbors=5)#, TODO: metric="mahalanobis", n_jobs=2) with covariant matrices
train, test = model_selection.train_test_split(data, test_size=0.2, random_state=42)
model.fit(train)

def get_data(*args):
    print(args)