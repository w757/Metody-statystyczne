'''
Matematica - program do wykresow i obliczen


matrixpow

to do petla z n
podniesienie wartosci macierzy do potegi 
zapisanie wartosci i podniesienie do potegi 


'''

import numpy as np
import matplotlib.pyplot as plt

def poteguj_macierz(macierz, N):
    macierz = np.matrix(macierz)
    if macierz.shape[0] != macierz.shape[1]:
        raise ValueError("Macierz musi być kwadratowa")
    
    if N == 0:
        return np.identity(macierz.shape[0])
    if N == 1:
        return macierz

    wynik = macierz
    for _ in range(1, N):
        wynik = wynik * macierz

    return wynik

# Nowa macierz 3x3
macierz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Zakres wartości N
wartosci_N = range(1, 100)  # N od 1 do 20

# Rozmiar macierzy
rozmiar_macierzy = len(macierz), len(macierz[0])

# Słownik przechowujący wartości dla każdego elementu macierzy
wartosci_elementow = {(i, j): [] for i in range(rozmiar_macierzy[0]) for j in range(rozmiar_macierzy[1])}

# Obliczanie wartości dla każdego elementu macierzy
for N in wartosci_N:
    wynik = poteguj_macierz(macierz, N)
    for i in range(rozmiar_macierzy[0]):
        for j in range(rozmiar_macierzy[1]):
            wartosci_elementow[(i, j)].append(wynik[i, j])

# Ustawienie kolorów dla wykresów
kolory = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

# Tworzenie wykresu
plt.figure(figsize=(12, 8))
for i in range(rozmiar_macierzy[0]):
    for j in range(rozmiar_macierzy[1]):
        color_index = i * rozmiar_macierzy[1] + j
        if color_index < len(kolory):
            color = kolory[color_index]
        else:
            # Generowanie losowego koloru, jeśli skończą się kolory z listy
            color = np.random.rand(3,)
        plt.plot(wartosci_N, wartosci_elementow[(i, j)], marker='o', color=color, label=f'Element [{i}][{j}]')

plt.title('Wartości elementów macierzy 3x3 w zależności od N')
plt.xlabel('N')
plt.ylabel('Wartość')
plt.legend()
plt.grid(True)
plt.show()
