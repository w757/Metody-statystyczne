import random
import matplotlib.pyplot as plt
from module import module
import numpy as np
 
a = 50
b = 50

data = []
p_values = np.linspace(0.01, 0.99, 100)

for p in p_values:
    maxLength = 0

    for _ in range (1000):
        maxLength = max(maxLength, module.gameSimulationGameLength (a, b, p))
    
    data.append(maxLength)



plt.figure(figsize=(6,6))
plt.bar(p_values, data, width=0.1)
plt.show()


    
