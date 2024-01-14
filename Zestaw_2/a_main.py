
import numpy as np
import matplotlib.pyplot as plt

# Inicjalizacja macierzy stochastycznej
C = np.array([[0.3, 0.6, 0.1],
              [0.5, 0.2, 0.3],
              [0.2, 0.45, 0.35]])

# Zakres wartości N
N_values_markov = range(0, 10)  

# Listy do przechowywania wartości wszystkich elementów macierzy
elements_C = []

# Obliczanie potęg macierzy przez kolejne mnożenie
for N in N_values_markov:
    if N == 0:
        # Dla N=0 używamy macierzy jednostkowej, ponieważ każda macierz do potęgi 0 daje macierz jednostkową
        powered_matrix = np.identity(C.shape[0])
    else:
        powered_matrix = np.linalg.matrix_power(C, N)
    
    # Dodanie wszystkich elementów z aktualnie potęgowanej macierzy
    elements_C.append(powered_matrix.flatten())

# Przygotowanie danych do wykresu
elements_C = np.array(elements_C)

# Tworzenie wykresów dla każdego elementu
plt.figure(figsize=(14, 8))

for i in range(C.shape[0]):
    for j in range(C.shape[1]):
        plt.plot(N_values_markov, elements_C[:, i * C.shape[1] + j], marker='o', label=f'Element C({i},{j})')


plt.xlabel('N')
plt.ylabel('Wartość elementu')
plt.legend(bbox_to_anchor=(1.04,0.5), loc="center left", borderaxespad=0)
plt.grid(True)
plt.tight_layout()
plt.show()
