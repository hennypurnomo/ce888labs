### vehicles.py

This file is used to retrieve data from vehicles.csv and create a scatterplots and histogram. The data contains some values of current and new fleet. The results will be saved in png and pdf file. It also print the result of mean, median, var, std, and Median Absolute Deviation (MAD). In order to deal with some missing values in the data, those values was converted into n/a and removed it with the function called dropna(). 

![logo](./vehiclesscaterplot.png?raw=true)

This image represents a scaterplot from vehicles.csv.

![logo](./vehicleshistogram.png?raw=true)

This image shows a histogram from vehicles.csv.

Index(['Current fleet', ' New Fleet'], dtype='object')

Mean: 30.481013

Median: 32.000000

Var: 36.831918

std: 6.068931

MAD: 4.000000

This is the result of mean, median, var, std and mad.




### bootstrapvehicles.py

This file is used to simulate data from vehicles.csv and calculate the standard deviation (STD) for current and new fleet with 10000 iteration. Because of some missing values in new fleet data, nan values was omitted with logical-not(np.isnan) function. 

Current Fleet Standard Deviation : 20.14457831325301

Current Fleet Upper Bound: 6.935700532006677

Current Fleet Lower Bound 5.799709966677345

New Fleet Standard Deviation : 30.481012658227847

New Fleet Upper Bound: 6.8793514727736085

New Fleet Lower Bound 5.1605477376344036

This is the result of Standard Deviation, upper bound and lower bound of those two kinds of fleet.

