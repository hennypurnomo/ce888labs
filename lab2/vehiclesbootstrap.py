#Removing the nan values in array from melissaOu on https://stackoverflow.com/questions/11620914/removing-nan-values-from-an-array

import matplotlib
matplotlib.use('Agg')

import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np 

def boostrap(statistic_func, iterations, data):
	samples  = np.random.choice(data,replace = True, size = [iterations, len(data)])
	#print samples.shape
	data_mean = data.mean()
	vals = []
	for sample in samples:
		sta = statistic_func(sample)
		#print sta
		vals.append(sta)
	b = np.array(vals)
	#print b
	lower, upper = np.percentile(b, [2.5, 97.5])
	return data_mean,lower, upper



if __name__ == "__main__":
	df = pd.read_csv('./vehicles.csv')
	#Obtaining the values from current fleet
	data = df.values.T[0]	
	boots = []
	boots = boostrap(np.std,10000,data)
	print("current fleet stander: ",boots[0])
	print("lower bound: ",boots[1])
	print("upper bound: ",boots[2])
	
	#Obtaining the values from new fleet
	data = df.values.T[1]	
	data = data[np.logical_not(np.isnan(data))] #removing NAN values
	boots = []
	boots = boostrap(np.std,10000,data)
	print("new fleet stander: ",boots[0])
	print("lower bound: ",boots[1])
	print("upper bound: ",boots[2])
