import random
import matplotlib.pyplot as plt
from module import module
import numpy as np


def probabilityFunction (a, b, p, n):
    z = a + b
    return(1 - a/z)


p = 0.5
a = 0

gameSimulationArray = []
probabilityFunctionArray  =[] 


a_values = np.linspace(1, 100, 100) 

n = 10

for a in a_values:
    b = 100 - a
    probabilityFunctionArray.append(probabilityFunction(a,b,p,n))

    gameSimulationArray.append(module.gameSimulation(a, b, p, n))
    


plt.figure(figsize=(10, 6))
plt.plot(a_values, gameSimulationArray, 'r')
plt.plot(a_values, probabilityFunctionArray, 'b')
plt.show()



'''
r(n) = 1 - n/z

p==q


r(n) - prawdopodobienstwo ruiny gracza z kapitalem poczatkowym n
z - calkowity kalpital dwoch graczy
p - prawdopodobienstwo wygranej gracza A
q - prawdopodobienstwo wygranej gracza B
p = 1 - q

'''