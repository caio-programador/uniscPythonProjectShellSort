from time import time

import numpy as np
from numpy import random as rd


def bubble_sort(vetor):
    n = len(vetor)
    troca = True
    while troca:
        troca = False
        for i in range(n - 1):
            if vetor[i] > vetor[i + 1]:
                vetor[i], vetor[i + 1] = vetor[i + 1], vetor[i]
                troca = True
        n -= 1
    return vetor


def insertion_sort(vetor):
    pass


#  para o quick sort
def particao(vetor, inicio, final):
    pass


def quick_sort(vetor, inicio, final):
    # desenvolver
    return vetor


def merge_sort(vetor):
    pass


def shell_sort(vetor):
    tamanho = len(vetor)  # Pega tamanho do vetor
    meio = tamanho // 2  # encontra o meio do vetor

    while meio > 0:  # percorre e vai dividindo esse meio por 2 enquanto ele for menor q 0
        for i in range(meio, tamanho):  # percorre a partir do meio
            aux = vetor[i]  # auxiliar
            j = i
            while j >= meio and vetor[j - meio] > aux:  # se o número na posicao j - a metade for maior
                vetor[j] = vetor[j - meio]  # entao troca
                j -= meio  # e j vai diminuindo
            vetor[j] = aux
        meio //= 2

    return vetor  # retorna o vetor ordenado


#  ele pega os menores valores e vai pondo nas menores posicoes
#  faz pesquisa sequencial para achar os menores valores
def selection_sort(vetor):
    pass


def radix_sort(vetor):
    pass


#  def PROXIMO_sort(vetor):

print()
# Para testar: Lista de números em ordem aleatória.
vetor1 = np.array([8, 5, 1, 7, 9, 4, 10, 3, 6, 2])
print(vetor1)
print("\nSHELL SORT")
inicio = time()
sort1 = shell_sort(vetor1)
total = time() - inicio
print(sort1)

print(total)

print("\nBUBBLE SORT")

inicio = time()
sort1 = bubble_sort(vetor1)
total = time() - inicio
print(sort1)

print(total)
print()
# Para testar: Uma lista que já está ordenada.
vetor2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(vetor2)
print("\nSHELL SORT")
inicio = time()
sort2 = shell_sort(vetor2)
total = time() - inicio
print(sort2)

print(total)

print("\nBUBBLE SORT")

inicio = time()
sort2 = bubble_sort(vetor2)
total = time() - inicio
print(sort2)

print(total)
print()
# Para testar: Uma lista classificada em ordem decrescente.
vetor3 = np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
print(vetor3)
print("\nSHELL SORT")
inicio = time()
sort3 = shell_sort(vetor3)
total = time() - inicio
print(sort3)

print(total)

print("\nBUBBLE SORT")

inicio = time()
sort3 = bubble_sort(vetor3)
total = time() - inicio
print(sort3)

print(total)
print()
# Para testar: Uma lista contendo elementos repetidos.
vetor4 = np.array([8, 5, 1, 7, 9, 4, 10, 3, 6, 2, 8, 5, 1])
print(vetor4)

print("\nSHELL SORT")
inicio = time()
sort4 = shell_sort(vetor4)
total = time() - inicio
print(sort4)

print(total)

print("\nBUBBLE SORT")

inicio = time()
sort4 = bubble_sort(vetor4)
total = time() - inicio
print(sort4)

print(total)
print()
# Para testar: Uma lista vazia.
vetor5 = np.array([])
print(vetor5)
print("\nSHELL SORT")
inicio = time()
sort5 = shell_sort(vetor5)
total = time() - inicio
print(sort5)

print(total)

print("\nBUBBLE SORT")

inicio = time()
sort5 = bubble_sort(vetor5)
total = time() - inicio
print(sort5)

print(total)
print()
# Para testar: Uma lista contendo apenas um elemento.
vetor6 = np.array([5])
print(vetor6)
print("\nSHELL SORT")
inicio = time()
sort6 = shell_sort(vetor6)
total = time() - inicio
print(sort6)

print(total)

print("\nBUBBLE SORT")

inicio = time()
sort6 = bubble_sort(vetor6)
total = time() - inicio
print(sort6)

print(total)
print()
# Para testar: Uma lista contendo um elemento repetido muitas vezes.
vetor7 = np.array([6, 9, 6, 7, 6, 5, 6, 6, 2, 6])
print(vetor7)
print("\nSHELL SORT")
inicio = time()
sort7 = shell_sort(vetor7)
total = time() - inicio
print(sort7)

print(total)

print("\nBUBBLE SORT")

inicio = time()
sort7 = bubble_sort(vetor7)
total = time() - inicio
print(sort7)

print(total)
print()
# Para testar: Uma lista longa.
vetor8 = rd.randint(0, 1000, 100)
print(vetor8)
print("\nSHELL SORT")
inicio = time()
sort8 = shell_sort(vetor8)
total = time() - inicio
print(sort8)

print(total)

print("\nBUBBLE SORT")

inicio = time()
sort8 = bubble_sort(vetor8)
total = time() - inicio
print(sort8)

print(total)
print()
