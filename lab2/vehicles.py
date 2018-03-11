#Removing the nan values in array from melissaOu on https://stackoverflow.com/questions/11620914/removing-nan-values-from-an-array

import matplotlib
matplotlib.use('Agg')

import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np 




# def permutation(statistic, error):


def mad(arr):
    """ Median Absolute Deviation: a "Robust" version of standard deviation.
        Indices variabililty of the sample.
        https://en.wikipedia.org/wiki/Median_absolute_deviation 
        http://stackoverflow.com/questions/8930370/where-can-i-find-mad-mean-absolute-deviation-in-scipy
    """
    arr = np.ma.array(arr).compressed() # should be faster to not use masked arrays.
    med = np.median(arr)
    return np.median(np.abs(arr - med))


if __name__ == "__main__":
	df = pd.read_csv('./vehicles.csv')
	ndf = df.dropna()	#Removing NAN values
	print (ndf.columns)
	sns_plot = sns.lmplot(ndf.columns[0], ndf.columns[1], data=ndf, fit_reg=False) #creating scaterplot

	sns_plot.axes[0,0].set_ylim(0,)
	sns_plot.axes[0,0].set_xlim(0,)

	sns_plot.savefig("vehicles_scaterplot.png",bbox_inches='tight')	#save in png
	sns_plot.savefig("vehicles_scaterplot.pdf",bbox_inches='tight')	#save in pdf
	
	plt.xlabel('current fleet')
	plt.ylabel('Proposed fleet')
	
	data = ndf.values.T[1]
	
	print (("Mean: %f")%(np.mean(data)))
	print (("Median: %f")%(np.median(data)))
	print (("Var: %f")%(np.var(data)))
	print (("std: %f")%(np.std(data)))
	print (("MAD: %f")%(mad(data)))

	plt.clf()
	sns_plot2 = sns.distplot(data, bins=20,kde=False, rug=True).get_figure() #creating histogram

	axes = plt.gca()
	axes.set_xlabel('current fleet') 
	axes.set_ylabel('proposed fleet')

	sns_plot2.savefig("vehicles_histogram.png",bbox_inches='tight')
	sns_plot2.savefig("vehicles_histogram.pdf",bbox_inches='tight')
