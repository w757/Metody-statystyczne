import random
import matplotlib.pyplot as plt
from module import module
import numpy as np
 
a = 50
b = 50

data = []
index = []
n = 30
i = 0
for i in range (n):
    p = i/n
    maxLength = 0
    for _ in range (1000):
        maxLength = max(maxLength, module.gameSimulationGameLength (a, b, p))
    
    data.append(maxLength)
    index.append(p)


plt.figure(figsize=(6,6))
plt.bar(index, data, width=0.1)
plt.show()


    
