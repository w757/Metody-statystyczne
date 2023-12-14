import matplotlib.pyplot as plt
import numpy as np
from module import module

def probabilityFunction(a, b, p):

    z = a + b
    n = a
    q = 1 - p

    result = ((q/p)**n - (q/p)**z) / (1 - (q/p)**z)
    return result


a = 50
b = 50
n = 10

p_values = np.linspace(0.01, 0.99, 100)     #  0.01 - 0.99

gameSimulationArray = []
probabilityFunctionArray = []

for p in p_values:

    probabilityFunctionArray.append( probabilityFunction(a, b, p))

    gameSimulationArray.append(module.gameSimulation(a, b, p, n))



plt.figure(figsize=(10, 6))
plt.plot(p_values, gameSimulationArray, 'r')
plt.plot(p_values, probabilityFunctionArray, 'b')

plt.show()
