import os
import numpy as np
import pandas

#IMPORT FILE
fp = '/Users/alexandermclaughlin/apps/hardway/test1.csv'
#
#
# #ISO-8859-1
# #possible encoding
df = pandas.read_csv(fp, encoding='Latin-1')
#
#     print (type(df))
print (df.head())
#
#     df = df.fillna('')
#     print (df.head())
#
titles = df['title'].value_counts()[:20]
print (titles)
