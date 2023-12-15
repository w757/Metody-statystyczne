import random
import matplotlib.pyplot as plt
from module import module
import numpy as np
import matplotlib.colors as mcolors
 
a = 10
b = 10

data = []
maximum = 0
i = 1

for p in [0.2, 0.5, 0.8]:
    for i in range(4):
        data, length = module.gameSimulationCountWinn(a, b, p)

        maximum = max(length, maximum)
        plt.step( list(range(length)), data, label=f'i={i}')
        data = []

    plt.show()

