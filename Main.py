from time import time

import numpy as np
from numpy import random as rd


def shell_sort(vetor):
    tamanho = len(vetor)
    meio = tamanho // 2

    while meio > 0:
        for i in range(meio, tamanho):
            aux = vetor[i]
            j = i
            while j >= meio and vetor[j - meio] > aux:
                vetor[j] = vetor[j - meio]
                j -= meio
            vetor[j] = aux
        meio //= 2

    return vetor


# Para testar: Lista de números em ordem aleatória.
vetor1 = np.array([8, 5, 1, 7, 9, 4, 10, 3, 6, 2])
print(vetor1)


inicio = time()
sort1 = shell_sort(vetor1)
total = time() - inicio
print(sort1)

print(total)
# Para testar: Uma lista que já está ordenada.
vetor2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(vetor2)


inicio = time()
sort2 = shell_sort(vetor2)
total = time() - inicio
print(sort2)

print(total)
# Para testar: Uma lista classificada em ordem decrescente.
vetor3 = np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
print(vetor3)


inicio = time()
sort3 = shell_sort(vetor3)
total = time() - inicio
print(sort3)

print(total)
# Para testar: Uma lista contendo elementos repetidos.
vetor4 = np.array([8, 5, 1, 7, 9, 4, 10, 3, 6, 2, 8, 5, 1])
print(vetor4)


inicio = time()
sort4 = shell_sort(vetor4)
total = time() - inicio
print(sort4)

print(total)
# Para testar: Uma lista vazia.
vetor5 = np.array([])
print(vetor5)


inicio = time()
sort5 = shell_sort(vetor5)
total = time() - inicio
print(sort5)

print(total)
# Para testar: Uma lista contendo apenas um elemento.
vetor6 = np.array([5])
print(vetor6)

inicio = time()
sort6 = shell_sort(vetor6)
total = time() - inicio
print(sort6)

print(total)
# Para testar: Uma lista contendo um elemento repetido muitas vezes.
vetor7 = np.array([6, 9, 6, 7, 6, 5, 6, 6, 2, 6])
print(vetor7)

inicio = time()
sort7 = shell_sort(vetor7)
total = time() - inicio
print(sort7)

print(total)
# Para testar: Uma lista longa.
vetor8 = rd.randint(0, 1000, 100)
print(vetor8)

inicio = time()
sort7 = shell_sort(vetor8)
total = time() - inicio
print(sort7)

print(total)
