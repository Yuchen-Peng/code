import pandas as pd
pd.__version__
import numpy as np

# check categorical variables: what are the unique categories.
df['category'].unique()

# create a dataframe which contains multiple groupby
df_groupby = df.groupby([col1, col2]).agg(['mean', 'count','std', 'min', 'max'])

# check float type nan
import math
x=float('nan')
math.isnan(x)

# applying pandas qcut bins determined from a benchmark data to new data
ser, bins = pd.qcut(df_ben["A"], 5, retbins=True, labels=False) # here bins is a 6-length array label the bin edges
pd.cut(df_new["A"], bins=bins, labels=False, include_lowest=True)

# count in bins
bin_count = pd.qcut(df_ben["A"], 5)["A"].value_counts()
bin_count = df_ben["A"].value_counts(bins = bins) # here bins is the bins created
# specify value_counts(sort=False) if loop through value_counts is needed

# duplicates = 'drop' will sometimes create less than specified bins if bin edges are not unique
# available for pandas version >= 0.20.0
bin_count = pd.qcut(df[var],5,duplicates='drop').value_counts(sort=False)

# object / str missing to float
 s
Out[11]: 
0    103.8
1    751.1
2      0.0
3      0.0
4        -
5        -
6      0.0
7        -
8      0.0
dtype: object

s.convert_objects(convert_numeric=True)
Out[12]: 
0    103.8
1    751.1
2      0.0
3      0.0
4      NaN
5      NaN
6      0.0
7      NaN
8      0.0
dtype: float64
 
 # sum over multiple column
 col_list_2015=list(df_houseprice[['2015-01','2015-02','2015-03','2015-04','2015-05','2015-06','2015-07','2015-08','2015-09','2015-10','2015-11','2015-12']])
 df_houseprice['avg_price_2015'] = 1/12*df_houseprice_141516[col_list_2015].sum(axis=1)
 
 # fillna for missing 
 
 df.fillna(0)
 df.fillna(method='ffill') / df.fillna(method='bfill') # Fill gaps forward or backward
 
 df.dropna()
 df.dropna(how='all') # only drop rows with all data missing
 
 # time stamp
 
from datetime import datetime
pd.Timestamp(datetime(2012, 5, 1))
Timestamp('2012-05-01 00:00:00')

# str date to datetime type
df['date_time'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

# dataframe groupby aggregation: mean, std
df = pd.DataFrame({'A':[1,1,2,2],'B':[1,2,1,2],'values':np.arange(10,30,5)})
df.groupby('A').agg(np.std)
value_std = df.groupby('A').agg(np.std)['values'].values # return the std's group by A as an array

# Re-order columns
dict1 = {'a':[1,2],'b':[0,10]}
df1 = pd.DataFrame(dict1)
df1['Segment'] = 'lalala'
cols = df1.columns.tolist()
cols = cols[-1:] + cols[:-1]
df1_new = df1[cols]

# Create dataframe from dictionary of dictionaries
movie_dict = {'Jill': {'Django Unchained': 6.5, 'Gone Girl': 9.0, 'Kill the Messenger': 8.0, 'Avenger: Age of Ultron': 7.0}, 'Toby': {'Django Unchained': 9.0, 'Zoolander': 2.0, 'Avenger: Age of Ultron': 8.5}}
movie_df = pd.DataFrame.from_dict(movie_dict, orient='index') # with movie_dict.keys to be the index
movie_df.index.name = 'Name' # Set the index to be the first column
movie_df = movie_df.reset_index()

# Create dataframe from list of dictionaries
list_rows = []
for i in range(5):
    dict1 = {'A':i,'B':i+1}
    list_rows.append(dict1)
df_fromlist = pd.DataFrame(list_rows) 
df_fromlist
Out[4]: 
   A   B
0  0   1
1  1   2
2  2   3
3  3   4
4  4   5

#output index of a series (to list, e.g.)
s1.index.tolist()
#e.g. output the index of value_counts
count = df['category'].value_counts()
count[0:10].index.tolist()


#iterate through index and column value
s = df[var].value_counts()
for index, val in s.iteritems():
    print index, val

#series (such as value.counts())to dataframe
dataframe[column].value_counts().to_frame()

#subset a dataframe, with value in/not in a list
df = pd.DataFrame({'countries':['US','UK','Germany','China','Japan']})
asian_countries = ['Japan','China']

df[df.countries.isin(asian_countries)]
df[~df.countries.isin(asian_countries)]

# subset a dataframe, with column contains a particular string
df = pd.DataFrame({'a':['abc','efg'],'b':[0,10]})
df[df['a'].str.contains('abc')]

#visualization
import matplotlib.pyplot as plt
%matplotlib inline # always include this in a notebook to display figures in the notebook

ax1 = df['value'].plot.kde() # e.g. plot density
ax1.set_xlabel('value')
ax1.set_ylabel('Frequency')

# plot scatter matrix
scatter = pd.scatter_matrix(X_train, c= y_train, marker = 'o', s=40, hist_kwds={'bins':15}, figsize=(5,5))
