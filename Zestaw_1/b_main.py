import random
import matplotlib.pyplot as plt
from module import module

def probabilityFunction(a, b, p):
    q = 1-p
    z = a+b 
    n = a

    if (p/q)**z==1:
        return "ss"
    else:
        return ( ((p/q)**n - (p/q)**z)  /  (1 - (p/q)**z) )


a = 5
b = 5

gameSimulationArray = []
probabilityFunctionArray = []
p_index = []
i = 1
n = 100

for i in range (n):
    p = i/n
    probabilityFunctionArray.append( probabilityFunction(a,b,p))
    p_index.append(p)
    gameSimulationArray.append(module.gameSimulation(a, b, p, n))

print (p_index)
print (probabilityFunctionArray)
print (gameSimulationArray)
plt.figure(figsize=(10, 6))
plt.plot(p_index, gameSimulationArray, 'r')
plt.plot(p_index, probabilityFunctionArray, 'b')

plt.show()





'''
r(n) = [ (p/q)^n - (p/q)^z ] / [1 - (p/q)^z]

p!=q


r(n) - prawdopodobienstwo ruiny gracza z kapitalem poczatkowym n
z - calkowity kalpital dwoch graczy
p - prawdopodobienstwo wygranej gracza A
q - prawdopodobienstwo wygranej gracza B
p = 1 - q
'''