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
