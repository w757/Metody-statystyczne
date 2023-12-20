import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Generate 10000 random numbers - N(0,1) 
numbers = np.random.normal(0, 1, 10000)

# Calculate the histogram
y, x = np.histogram(numbers, bins=50, density=True)
x = (x + np.roll(x, -1))[:-1] / 2.0

# Calculate probability density function
pdf = norm.pdf(x, 0, 1)


plt.hist(numbers, bins=50, density=True, alpha=0.6, color='b')  #density=True - normalizacja do 1
plt.plot(x, pdf, 'r')

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
