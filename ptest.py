import numpy as np
from scipy.stats import ttest_1samp
import seaborn as sns
import matplotlib.pyplot as plt 

ages = np.random.choice(80,10)
sample_size = 10

age_sample = np.random.choice(ages,sample_size)

print(age_sample)

mean = np.mean(age_sample)
print(mean)
s,p = ttest_1samp(age_sample,30)##ttest

print(p)
if p< 0.05:
    print("reject H0")
else:
    print("accept")

##
    df = sns.load_dataset('iris')
    df_numeric = df.drop(columns='species')
    df1 = df_numeric.head(30)

    print(df1.corr())

    plot = df1.corr()

    sns.pairplot(plot)

    plt.show()