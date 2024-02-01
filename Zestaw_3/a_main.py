import random
import math
import matplotlib.pyplot as plt
# uwzglednic wolne naplywanie, szybkie i stale 

lambda_A = 1/30
lambda_S = 1/20

tasks = range(0, 10) 



czas_oczekiwania_tab1 = []
czas_oczekiwania_tab2 = []

ilosc = []

sum_kolejka= 0 
czas_oczekiwania = 0

tmp1 =0 
tmp2 =0

for i in tasks:

    if (czas_oczekiwania > 0):
        sum_kolejka = sum_kolejka + 1
        ilosc.append(sum_kolejka)
    
    else:
        if (sum_kolejka > 0):
            sum_kolejka= sum_kolejka - 1
            ilosc.append(sum_kolejka)
        else:
            sum_kolejka = 0
            ilosc.append(sum_kolejka)


    t_i = (-1)*math.log(random.uniform(0, 1))/lambda_A 
    t_iS = (-1)*math.log(random.uniform(0, 1))/lambda_S


    # if (i==0):
    #     t_i = 0
    
    czas_oczekiwania = czas_oczekiwania + t_iS - t_i 


    tmp1 = tmp1 + t_i

    czas_oczekiwania_tab1.append(tmp1)

    tmp2 = tmp2 + t_iS + t_i

    czas_oczekiwania_tab2.append(tmp2)



plt.figure(figsize=(15, 5))



plt.scatter(czas_oczekiwania_tab2, ilosc, color='blue')
plt.scatter(czas_oczekiwania_tab1, ilosc, color='red')


plt.xlabel('Oś X')
plt.ylabel('Oś Y')
plt.title('Wykres punktowy')



plt.show()
