import random
import matplotlib.pyplot as plt
from module import module
import numpy as np



p = 0.5
a = 50
b = 50



for x in [1, 10, 50, 60, 70,80]:
    data = (module.gameSimulationArr (a, b, p, x))

    plt.hist(data, bins=30, edgecolor='black')
    plt.show()
