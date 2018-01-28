#Removing the nan values in array from melissaOu on https://stackoverflow.com/questions/11620914/removing-nan-values-from-an-array

import matplotlib
matplotlib.use('Agg')

import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np 




def bootstrap(statistic_func, iterations, data):
	samples  = np.random.choice(data,replace = True, size = [iterations, len(data)])
	#print (samples.shape)
	data_mean = data.mean()
	vals = []
	for sample in samples:
		sta = statistic_func(sample)
		#print (sta)
		vals.append(sta)
	b = np.array(vals)
	#print (b)
	lower, upper = np.percentile(b, [2.5, 97.5])
	return data_mean,lower, upper



if __name__ == "__main__":
	df = pd.read_csv('./vehicles.csv')
	#print (df.columns)
	
	data = df.values.T[0]   #getting the data for current fleet column
	boots = []
	boots = bootstrap (np.std,10000, data)   
	#print(boots) will print (STD, lower, upper)
	print("Current Fleet Standard Deviation :", boots[0]) 
	print("Current Fleet Upper Bound:" , boots[2])
	print("Current Fleet Lower Bound" , boots[1])


	data = df.values.T[1]   #getting the data for new fleet column
	data = data[np.logical_not(np.isnan(data))]    #removing nan values in array
	boots = []
	boots = bootstrap (np.std,10000, data)
	print("\nNew Fleet Standard Deviation :", boots[0])
	print("New Fleet Upper Bound:" , boots[2])
	print("New Fleet Lower Bound" , boots[1])

	
