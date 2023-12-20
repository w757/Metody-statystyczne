import random
import matplotlib.pyplot as plt
from module import module
import numpy as np
 
a = 50
b = 50

data = []

for p in [0.2, 0.5, 0.8]:
    data = []
    for i in range (2000):
        data.append(module.gameSimulationGameLength (a, b, p))


    avr = np.mean(data)
    plt.axhline(avr, color='red', linestyle='dashed', linewidth=2, label=f'Średnia = {avr}')
    plt.hist(data, bins=30, edgecolor='black')
    plt.show()
