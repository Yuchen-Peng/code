from matplotlib import pyplot as plt
import numpy as np
%matplotlib inline # always include this in a notebook to display figures in the notebook

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
    
# plot in a loop, grab in one subplot

category_lst = df['category'].value_counts().index.tolist()
#suppose we have 9 categories
fig, axs = plt.subplots(nrows=3, ncols=3,figsize=(20, 10))
for idx in range(len(category_lst)):
    df[df['category'] == category]['value'].plot.hist(bins = 10,ax = axs[idx//3][idx%3])
    axs[idx//3][idx%3].set_xlabel('value, %s category' %category)
    axs[idx//3][idx%3].set_ylabel('Count')
    plt.show()
