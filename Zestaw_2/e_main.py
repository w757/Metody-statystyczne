'''
t 1,2,3 - to sa liczby wylosowane z rozkladu poissona - wzor na slajdzie (losujemy liczbe z przedialu (0, 1 ) i podstawiamy do wzoru )

10^4 generujemy cale schodki 


jaki jest rozklad prawdopodobienstwa - na jakim schodku bedziemy stac dla t = .... na kazdym z 10^4 schodkow 

porownujemy wynik z rozkladem puasona 

# Parametr lambda
lambda_ = 1

# Zakres wartości k (liczba zdarzeń)
k_values = np.arange(0, 10)

# Obliczenie prawdopodobieństwa dla różnych wartości k z rozkładu Poissona
poisson_probabilities = [(np.exp(-lambda_) * lambda_**k) / np.math.factorial(k) for k in k_values]



# Rysowanie wykresu
plt.bar(k_values, poisson_probabilities)
plt.title('Rozkład Poissona dla λ = 1')
plt.xlabel('Liczba zdarzeń (k)')
plt.ylabel('Prawdopodobieństwo')
plt.show()


'''

import math
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

def generate_random_number():
    return random.uniform(0, 1)

lam = 1

final_tab = []

for i in range (1000):
    t = []
    sum = 0
    for j in range (10**4):
        rand = generate_random_number()
        sum += rand
        t.append(((-1 * math.log(rand)) / lam)+sum)
        final_tab.append(t)

wartosci_miejsce_1 = [t[0] for t in final_tab]
wartosci_miejsce_20 = [t[19] for t in final_tab]
wartosci_miejsce_90 = [t[89] for t in final_tab]

# Tworzenie histogramów
plt.figure(figsize=(15, 5))

# Zakres dla teoretycznego rozkładu Poissona
k_max = np.arange(0, 10)

# Rozkład Poissona dla porównania
poisson_distribution = poisson.pmf(k_max, lam)

# Histogram dla miejsca 1
plt.subplot(1, 3, 1)
plt.hist(wartosci_miejsce_1, bins=20, color='blue', density=True, alpha=0.5, label='Symulacja')
plt.plot(k_max, poisson_distribution, 'o-', color='black', label='Poisson')
plt.title('Histogram dla miejsca 1')
plt.legend()

# Histogram dla miejsca 20
plt.subplot(1, 3, 2)
plt.hist(wartosci_miejsce_20, bins=20, color='green', density=True, alpha=0.5, label='Symulacja')
plt.plot(k_max, poisson_distribution, 'o-', color='black', label='Poisson')
plt.title('Histogram dla miejsca 20')
plt.legend()

# Histogram dla miejsca 90
plt.subplot(1, 3, 3)
plt.hist(wartosci_miejsce_90, bins=20, color='red', density=True, alpha=0.5, label='Symulacja')
plt.plot(k_max, poisson_distribution, 'o-', color='black', label='Poisson')
plt.title('Histogram dla miejsca 90')
plt.legend()

plt.tight_layout()
plt.show()
