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
bin_count = pd.qcut(df_ben["A"], 5).value_counts()

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
