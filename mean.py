import numpy as np;

import matplotlib.pyplot as plt 


#%matplotlib inline

import statistics
import seaborn as sns

df = sns.load_dataset('tips')
print(df.head())

print(np.mean(df['total_bill']))
print(np.median(df['tip']))

print(statistics.mode(df['sex']))

print(statistics.stdev(df['total_bill']))
print(statistics.fmean(df['tip']))

# Set up the figure and axes 
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

sns.boxplot(df['total_bill'],ax=ax1)
ax1.set_title('Box Plot')
sns.histplot(df['total_bill'],ax = ax2,kde=False)
ax2.set_title('Histograph')

sns.histplot(df['tip'], ax=ax3,kde=True)
ax3.set_title('Scatter Plot')

plt.tight_layout()
plt.show()

sns.countplot(df['sex'])
plt.show()

print(np.percentile(df['total_bill'],[25,70]))

