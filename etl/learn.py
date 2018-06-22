# import re
# with open('sample_text.txt', 'r') as fp:
#     text = fp.read()
#
# pattern = re.compile(r'(?:href=\")(.*)(?:\"\sclass)')
# urls = pattern.findall(text)
# print urls

# import csv
#
# names = list()
#
# with open('names.csv', 'r') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row['name'], row['age'], row['property']

import pandas as pd
import numpy as np
import matplotlib.pylab as sample_text
#matplotlib inline
from matplotlib.pylab import rcParams
from datetime import datetime

rcParams['figure.figsize'] = 15,6

dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')

data = pd.read_csv('AirPassengers.csv', parse_dates=['Month'], index_col='Month', date_parser=dateparse)
print data.head()
print 'n\ Data Types:'
print data.dtypes
print data.index

#assign data to timeseries object
ts=data['#Passengers']
print ts.head(10)

#select a single value in a ts
print ts['1949-01-01']
print ts[datetime(1949,1,1)]
