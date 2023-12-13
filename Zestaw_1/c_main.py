import random
import matplotlib.pyplot as plt
from module import module


def probabilityFunction (a, b, p, n):
    z = a + b
    return(1 - a/z)


p = 0.5
a = 0
b = 0

gameSimulationArray = []
probabilityFunctionArray  =[] 
a_index = []

n = 100

for a in range (100):
    b = 100 - a
    gameSimulationArray.append(module.gameSimulation(a, b, p, n))
    probabilityFunctionArray.append(probabilityFunction(a,b,p,n))
    a_index.append(a)


plt.figure(figsize=(10, 6))
plt.plot(a_index, gameSimulationArray, 'r')
plt.plot(a_index, probabilityFunctionArray, 'b')
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