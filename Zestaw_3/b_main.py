import random
import math
import matplotlib.pyplot as plt
import statistics
# uwzglednic wolne naplywanie, szybkie i stale 

lambda_A = 1/20 #sredni czas wplywania zadania 
lambda_S = 1/15 # sredni czas wykonywania zadania

tasks = range(0, 100000) 

czas_oczekiwania_tab1 = []
czas_oczekiwania_tab2 = []
czas_spedzony_w_systemie = [] 

ilosc = []

sum_kolejka= 0 
czas_oczekiwania = 0

tmp1 =0 
tmp2 =0
k = 0
for i in tasks:
    k = k +1
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


    #### tu jest  bload w liczeniu czasu
    czas_oczekiwania = czas_oczekiwania + t_iS - t_i 


    tmp1 = tmp1 + t_i

    czas_oczekiwania_tab1.append(tmp1)

    tmp2 = tmp2 + t_iS + t_i

    czas_oczekiwania_tab2.append(tmp2)

    czas_spedzony_w_systemie.append(tmp1+tmp2) #czas oczekiwania + czas wykonywania 


    ########
    
sredni_czas_oczekiwania = statistics.mean(czas_spedzony_w_systemie)
print ("Ilosc klientw", k)
print ("sredni_czas_oczekiwania", sredni_czas_oczekiwania)
print ("lambda_A", lambda_A)
print (sredni_czas_oczekiwania*lambda_S)

plt.figure(figsize=(15, 5))



plt.scatter(czas_oczekiwania_tab2, ilosc, color='blue')
plt.scatter(czas_oczekiwania_tab1, ilosc, color='red')


plt.xlabel('Oś X')
plt.ylabel('Oś Y')
plt.title('Wykres punktowy')



plt.show()
