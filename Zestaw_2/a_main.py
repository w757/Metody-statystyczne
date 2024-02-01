import numpy as np
import matplotlib.pyplot as plt

# Inicjalizacja macierzy stochastycznej
C = np.array([[0.64, 0.32, 0.04],
              [0.4, 0.5, 0.1],
              [0.25, 0.5, 0.25]])


N_values_markov = range(0, 100) 

# Listy do przechowywania wartości wszystkich elementów macierzy
elements_C = []


previous_matrix = np.identity(C.shape[0]) # poprzednia macierz dla pierwszej iteracji 

for N in N_values_markov:
    powered_matrix = np.dot(previous_matrix, C) # dla pierwszej  iteracji macierz jednostkowa 
    
    # Dodanie wszystkich elementów z aktualnie potęgowanej macierzy
    elements_C.append(powered_matrix.flatten())

    # Sprawdzanie kryterium zbieżności
    if N > 0:
        if np.all(np.abs(powered_matrix - previous_matrix) < 1e-5):
            print(f"Kryterium zbieżności osiągnięte dla N={N}")
            break

    previous_matrix = powered_matrix

# Przygotowanie danych do wykresu
elements_C = np.array(elements_C)

# Tworzenie wykresów dla każdego elementu
plt.figure(figsize=(14, 8))

for i in range(C.shape[0]):
    for j in range(C.shape[1]):
        plt.plot(range(len(elements_C)), elements_C[:, i * C.shape[1] + j], marker='o', label=f'Element C({i},{j})')

plt.xlabel('N')
plt.ylabel('Wartość elementu')
plt.legend(bbox_to_anchor=(1.04,0.5), loc="center left", borderaxespad=0)
plt.grid(True)
plt.tight_layout()
plt.show()
