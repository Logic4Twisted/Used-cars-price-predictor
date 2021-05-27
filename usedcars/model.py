import numpy as np
import pandas as pd
import sklearn 
import pickle

from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_extraction import DictVectorizer
from sklearn import preprocessing
import joblib
import sys

data = pd.read_csv('./usedcars/data/autos_clean.csv', encoding='latin_1')
# columns: 
# name,
# price,
# vehicleType,
# yearOfRegistration,
# gearbox,
# powerPS,
# model,
# kilometer,
# fuelType,
# brand,
# age,
# daysOnEbay,
# brandModel,
# vehicleClass

"""
Index(['name', 'price', 'vehicleType', 'yearOfRegistration', 'gearbox',
       'powerPS', 'model', 'kilometer', 'fuelType', 'brand', 'age',
       'daysOnEbay', 'brandModel', 'vehicleClass'],
      dtype='object')
"""
data = data.dropna(subset=['vehicleType', 'gearbox', 'model', 'fuelType'], how='any')
data = data[(data.price >= 100) & (data.price <= 50000)]
data = data[(data.yearOfRegistration >= 1960) & (data.yearOfRegistration <= 2016)]
data = data[(data.powerPS >= 10) & (data.powerPS <= 500)]

data.dropna(inplace=True)

print(data.columns, file=sys.stderr)

def to_german(word):
	if word == 'Yes':
		return 'ja'
	if word == 'No':
		return 'nein'
	return 'not-specified'

def helper(input):
	filtered_data = data
	if input['fuel_type'] != '---':
		filtered_data = filtered_data[filtered_data['fuelType'] == input['fuel_type']]
	if input['gear_box'] != '---':
		filtered_data = filtered_data[filtered_data['gearbox'] == input['gear_box']]
	if input['vehicle_type'] != '---':
		filtered_data = filtered_data[filtered_data['vehicleType'] == input['vehicle_type']]
	if input['brand'] != '---':
		filtered_data = filtered_data[filtered_data['brand'] == input['brand'].strip()]
	if input['model'] != '---':
		filtered_data = filtered_data[filtered_data['model'] == input['model'].strip()]

	filtered_data = filtered_data[filtered_data['yearOfRegistration'] >= input['year_of_registration']]
	filtered_data = filtered_data[filtered_data['powerPS'] >= input['power_ps']]
	if str(input['kilometers']) != 'None':
		filtered_data = filtered_data[filtered_data['kilometer'] <= int(str(input['kilometers']))]
	if len(filtered_data.index) == 0:
		return dict()

	model_columns = joblib.load('./usedcars/data/model_columns.pkl')
	df = pd.DataFrame(columns=np.asarray(model_columns), index = filtered_data.index)
	df.fillna(0 ,inplace=True)

	for index, row in filtered_data.iterrows():
		df.loc[index]['yearOfRegistration'] = row['yearOfRegistration']
		df.loc[index]['powerPS'] = row['powerPS']
		df.loc[index]['kilometer'] = row['kilometer']
		df.loc[index]['brand=' + row['brand']] = 1.0
		df.loc[index]['fuelType=' + row['fuelType']] = 1.0
		df.loc[index]['gearbox=' + row['gearbox']] = 1.0
		df.loc[index]['model=' + row['model']] = 1.0
		df.loc[index]['vehicleType='+row['vehicleType']] = 1.0

	clf = joblib.load('./usedcars/data/regressor.pkl')
	pred = clf.predict(df)
	filtered_data['predicted_price'] = pred
	filtered_data['difference'] = filtered_data['price'] - filtered_data['predicted_price']
	filtered_data.sort_values(by = 'difference', inplace=True)
	print (filtered_data.columns)

	return filtered_data.to_dict(orient='index')