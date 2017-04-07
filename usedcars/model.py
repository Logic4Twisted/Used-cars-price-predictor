import numpy as np
import pandas as pd
import sklearn 
import pickle

from sklearn.feature_extraction import DictVectorizer
from sklearn import preprocessing
from sklearn.externals import joblib

data = pd.read_csv('./usedcars/data/autos.csv', encoding='latin_1')
data['notRepairedDamage'].fillna(value='not-specified', inplace=True)
data = data.dropna(subset=['vehicleType', 'gearbox', 'model', 'fuelType'], how='any')
data = data[(data.price >= 100) & (data.price <= 50000)]
data = data[(data.yearOfRegistration >= 1960) & (data.yearOfRegistration <= 2016)]
data = data[(data.powerPS >= 10) & (data.powerPS <= 500)]
data = data[(data.offerType != 'Gesuch') & (data.seller != 'gewerblich')]
data.drop(['seller', 'offerType'], axis = 1, inplace = True)
data.drop(['abtest'], axis='columns', inplace=True)
data.drop('lastSeen', axis=1, inplace=True)
data.drop('dateCreated', axis=1, inplace=True)
data.drop('nrOfPictures', axis=1, inplace=True)
data.drop('dateCrawled', axis=1, inplace=True)
data.dropna(inplace=True)

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
	if input['damage'] != 'Unknown':
		filtered_data = filtered_data[filtered_data['notRepairedDamage'] == to_german(input['damage'])]
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
		df.loc[index]['monthOfRegistration'] = row['monthOfRegistration']
		df.loc[index]['brand=' + row['brand']] = 1.0
		df.loc[index]['fuelType=' + row['fuelType']] = 1.0
		df.loc[index]['gearbox=' + row['gearbox']] = 1.0
		df.loc[index]['model=' + row['model']] = 1.0
		for xx in ['ja', 'nein', 'not-specified']:
			if to_german(row['notRepairedDamage']) == xx:
				df.loc[index]['notRepairedDamage='+xx] = 1.0
		df.loc[index]['vehicleType='+row['vehicleType']] = 1.0

	clf = joblib.load('./usedcars/data/regressor.pkl')
	pred = clf.predict(df)
	filtered_data['predicted_price'] = pred
	filtered_data['difference'] = filtered_data['price'] - filtered_data['predicted_price']
	filtered_data.sort(['difference'], inplace=True)

	return filtered_data.to_dict(orient='index')