import random
import matplotlib.pyplot as plt
from module import module
import numpy as np
 
a = 10
b = 10

data = []
counter = []

for p in [0.2, 0.5, 0.8]:
    for i in range (10):
        data.append(module.gameSimulationCountWinn (a, b, p))
        counter.append(i)


    plt.figure(figsize=(6, 6))
    # plt.plot(a_index, gameSimulationArray, 'r')
    # plt.plot(a_index, probabilityFunctionArray, 'b')
    plt.bar(counter, data, width=0.4)
    plt.show()
