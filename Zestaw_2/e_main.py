
import math
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson


lam = 1  
time_intervals = [1, 20, 90]  
num_simulations = 10**4

# Tworzenie histogramów dla różnych przedziałów czasu
plt.figure(figsize=(15, 5))


for i, time_interval in enumerate(time_intervals, 1):     # indeks + wartosc 

    # Generowanie liczby zdarzeń w określonym przedziale czasu dla każdej symulacji - num_simulations (10**4)
    event_counts = np.random.poisson(lam * time_interval, num_simulations)
    k_values = np.arange(0, max(event_counts) + 1)                  

    # rozkład Poissona ze wzoru
    poisson_prob = poisson.pmf(k_values, lam * time_interval)

    # Rysowanie histogramu dla danego przedziału czasu
    plt.subplot(1, 3, i)
    plt.hist(event_counts, bins=max(event_counts) - min(event_counts), density=True, alpha=0.5, color='blue', label=f'Symulacja dla t={time_interval}')
    plt.plot(k_values, poisson_prob, 'o-', color='black', label='Rozkład Poissona')
    plt.title(f't={time_interval}')
    plt.xlabel('Liczba zdarzeń')
    plt.ylabel('Prawdopodobieństwo')
    plt.legend()

plt.tight_layout()
plt.show()

















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


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Parametry
lam = 1  # Średnia liczba zdarzeń (lambda) na jednostkę czasu
total_time = 10  # Całkowity czas symulacji
num_simulations = 1000  # Zwiększona liczba symulacji dla lepszego przybliżenia

# Funkcja generująca liczbę zdarzeń w procesie Poissona dla każdej symulacji
def generate_poisson_events(lam, total_time):
    return np.random.poisson(lam * total_time)

# Generowanie danych
num_events = [generate_poisson_events(lam, total_time) for _ in range(num_simulations)]

# Teoretyczny rozkład Poissona do porównania
k_values = np.arange(0, max(num_events) + 1)
poisson_prob = poisson.pmf(k_values, lam * total_time)

# Tworzenie histogramu
plt.figure(figsize=(10, 6))
plt.hist(num_events, bins=max(num_events) - min(num_events), density=True, alpha=0.5, color='blue', label='Symulacja')
plt.plot(k_values, poisson_prob, 'o-', color='black', label='Rozkład Poissona')
plt.title('Histogram liczby zdarzeń w procesie Poissona vs Teoretyczny rozkład Poissona')
plt.xlabel('Liczba zdarzeń')
plt.ylabel('Prawdopodobieństwo')
plt.legend()
plt.show()


'''