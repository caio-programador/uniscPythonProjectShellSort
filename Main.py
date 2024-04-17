from time import time

import numpy as np
from numpy import random as rd

from time import time


def bubble_sort_lento(array):
    # loop to access each array element
    for i in range(len(array)):

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:
                # swapping elements if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array


def bubble_sort_otimizado(vetor):
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
    n = len(vetor)

    for index in range(n):
        valorAtual = vetor[index]
        posicao = index

        while posicao > 0 and vetor[index+1]<valorAtual:
            vetor[index+1] = vetor[index]
            posicao-=1
        vetor[index] = valorAtual

    return vetor


#  para o quick sort
def particao(vetor, inicio, final):
    pass


def quick_sort(vetor, inicio, final):
    # desenvolver
    return vetor


def merge_sort(vetor):
    pass


def shell_sort(vetor):
    h = len(vetor) // 2
    while h > 0:

        for start in range(h):
            for i in range(start + h, len(vetor), h):

                currentvalue = vetor[i]
                position = i

                while position >= h and vetor[position - h] > currentvalue:
                    vetor[position] = vetor[position - h]
                    position = position - h

                vetor[position] = currentvalue

        h = h // 2

        return vetor






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
sort1 = bubble_sort_otimizado(vetor1)
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
sort2 = bubble_sort_otimizado(vetor2)
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
sort3 = bubble_sort_otimizado(vetor3)
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
sort4 = bubble_sort_otimizado(vetor4)
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
sort5 = bubble_sort_otimizado(vetor5)
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
sort6 = bubble_sort_otimizado(vetor6)
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
sort7 = bubble_sort_otimizado(vetor7)
total = time() - inicio
print(sort7)

print(total)
print()
# Para testar: Uma lista longa.
vetor8 = rd.randint(0, 1000000, 100000)
print(vetor8)
print("\nSHELL SORT")
inicio = time()
sort8 = shell_sort(vetor8)
total = time() - inicio
print(sort8)

print(total)

print("\nBUBBLE SORT")

inicio = time()
sort8 = bubble_sort_otimizado(vetor8)
total = time() - inicio
print(sort8)

print(total)
print()

print("\nINSERTION SORT")

inicio = time()
sort8 = insertion_sort(vetor8)
total = time() - inicio
print(sort8)

print(total)
print()
