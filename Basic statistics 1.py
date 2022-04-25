"""

Wellcome to coding

"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


np.random.seed(1)
data = np.round(np.random.normal(5, 2, 100))
plt.hist(data, bins=10, range=(0,10), edgecolor='black')
plt.show()


# Mean
mean = np.mean(data)
print(mean)

# Median
median = np.median(data)
print(median)

# Mode
mode = stats.mode(data)
print(mode)

# Variance
var = np.var(data)
print(var)

# Standard Deviation
sd = np.std(data)
print(sd)
