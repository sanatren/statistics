import numpy as np
from statsmodels.stats.weightstats import ztest

data = np.random.randint(0, 150, 20)  # Generate 20 random integers between 0 and 149
print("Data:", data)

sample_mean = np.mean(data)
print("Sample mean:", sample_mean)

# Perform the z-test, testing against a population mean of 80
z_statistic, p_val = ztest(data, value=80)

if p_val < 0.05:
    print("Reject H0")
else:
    print("Accept H0")