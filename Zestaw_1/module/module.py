import random

'''Funkcja zwraca prawdopodobienstwo ruiny gracza A'''

def gameSimulation(a, b, p, n):  

    a_temp, b_temp = a, b
    sum_A = 0.0
    sum_B = 0.0

    for _ in range (n):
        a_temp = a
        b_temp = b

        while a_temp > 0 and b_temp > 0:
            rand = random.uniform(0,1)

            if rand < p:
                a_temp += 1
                b_temp -= 1
            else:
                a_temp -= 1
                b_temp += 1

        if a_temp == 0:
            sum_B +=1
        else:
            sum_A +=1
        
    return (sum_B/n)


'''Funkcja zwraca dugosc rozgrywki'''

def gameSimulationGameLength (a, b, p):  

    a_temp, b_temp = a, b
    length = 0

    while a_temp > 0 and b_temp > 0:
        rand = random.uniform(0,1)
        length +=1

        if rand < p:
            a_temp += 1
            b_temp -= 1
        else:
            a_temp -= 1
            b_temp += 1
            
    return (length)