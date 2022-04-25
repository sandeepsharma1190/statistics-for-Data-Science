import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt


np.random.seed(1)
data = np.round(np.random.normal(5, 2, 100))

# Variance
var = np.var(data)
print(var)


# Standard Deviation
sd = np.std(data)
print(sd)


# Quantiles
# Creating the dataframe
df = pd.DataFrame({"A":[1, 5, 3, 4, 2],
                   "B":[3, 2, 4, 3, 4],
                   "C":[2, 2, 7, 3, 4],
                   "D":[4, 3, 6, 12, 7]})

df.quantile(.2, axis = 0)
df.quantile([.1, .25, .5, .75], axis = 0)


# Skewness
x1 = np.linspace( -5, 5, 1000 ) 
y1 = 1./(np.sqrt(2.*np.pi)) * np.exp( -.5*(x1)**2  ) 
plt.plot(x1, y1)
print(stats.skew(y1))


# Kurtosis
x1 = np.linspace( -5, 5, 1000 )
y1 = 1./(np.sqrt(2.*np.pi)) * np.exp( -.5*(x1)**2  )
plt.plot(x1, y1, '*')
print(stats.kurtosis(y1))
