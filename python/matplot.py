from matplotlib import pyplot as plt
import numpy as np
%matplotlib inline # always include this in a notebook to display figures in the notebook
%matplotlib notebook # this will activate an interactive plot mode
import seaborn as sns
sns.set() # to give gray background figures


# Notation on scatter points
x=np.random.uniform(0,1,5)
y=np.random.uniform(0,1,5)
note=['p1','p2','p3','p4','p5']

fig, ax = plt.subplots()
ax.scatter(x, y)
ax.set_xlabel('X')
ax.set_ylabel('Y')
for i, txt in enumerate(note):
    ax.annotate(txt, (x[i],y[i]))

#plot function
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.show()

#plot in a loop

category_lst = df['category'].value_counts().index.tolist()

for category in category_lst:
    ax = df[df['category'] == category]['value'].plot.hist(bins = 10)
    ax.set_xlabel('value, %s category' %category)
    ax.set_ylabel('Count')
    plt.show()
    
# plot in a loop, multiple subplots in one big plot

category_lst = df['category'].value_counts().index.tolist()
#suppose we have 9 categories
fig, axs = plt.subplots(nrows=3, ncols=3,figsize=(20, 10))
for idx in range(len(category_lst)):
    df[df['category'] == category]['value'].plot.hist(bins = 10,ax = axs[idx//3][idx%3])
    axs[idx//3][idx%3].set_xlabel('value, %s category' %category)
    axs[idx//3][idx%3].set_ylabel('Count')
    plt.show()

# save axe classs to image file (such as xgboost importance figure)
importance = xgb.plot_importance(fitted,max_num_features=20) # importance is a matplotlib axe object
fig = importance.get_figure()
fig.savefig("./images/FS_feature_imp.png",dpi=fig.dpi,bbox_inches='tight')

# Scatter plot; size of the scatter also depend on data
# In this example, we scatter income vs spend in each cluster; the size of scatter is the number of people in each cluster.
plt.figure(figsize=(10,8))

for i in range(1,11):
    plt.scatter(df_cluster['Income'].loc[i], df_cluster['Spend'].loc[i], s=df_cluster['Count'].loc[i], alpha=0.5, label=i)

plt.xlabel("Average of Income in each cluster")
plt.ylabel("Average of Spend in each cluster")
