import matplotlib.pyplot as plt
import numpy as np
from numpy.random import normal
from numpy import mean, std
from scipy.stats import norm

sample = normal(loc=50, scale=5, size=1000)

plt.figure(figsize=(8, 6))  
plt.hist(sample, bins=10, density=True, alpha=0.6, label='Sample Histogram')

sample_mean = mean(sample)
sample_std = std(sample)

print('Mean=%.3f \nStandart Deviation=%.3f' % (sample_mean, sample_std))

dist = norm(sample_mean, sample_std)

values = [value for value in range(30, 70)]

probabilitas = [dist.pdf(value) for value in values]

print(probabilitas)

plt.plot(values, probabilitas, label='Normal Distribution', color='red', linewidth=2)

plt.title('Histogram and Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.legend()

plt.show()