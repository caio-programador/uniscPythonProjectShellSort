from time import time
import timeit

from Sort.Sort import *


def ordena(sortType, vetor):
    novoVetor = vetor.copy()

    match sortType:
        case 1:
            print("\nBUBBLE SORT")
            inicio = time()
            novoVetor, comparacoes, trocas = bubble_sort(novoVetor)
            total = time() - inicio
            print(f'{novoVetor}\n- Trocas: {trocas}\n- Comparações: {comparacoes}\n- Tempo de resposta: {total}')
        case 2:
            print("\nSHELL SORT")
            inicio = time()
            novoVetor, comparacoes, trocas = shell_sort(novoVetor)
            total = time() - inicio
            print(f'{novoVetor}\n- Trocas: {trocas}\n- Comparações: {comparacoes}\n- Tempo de resposta: {total}')
        case 3:
            inicio = time()
            quick_sort(novoVetor)
        case 4:
            print("\nINSERTION SORT")
            inicio = time()
            vetor, comparacoes, trocas = insertion_sort(novoVetor)
            total = time() - inicio
            print(f'{vetor}\n- Trocas: {trocas}\n- Comparações: {comparacoes}\n- Tempo de resposta: {total}')
        case 5:
            inicio = time()
            merge_sort(novoVetor)
        case 6:
            inicio = time()
            selection_sort(novoVetor)
        case 7:
            # inicio = time()
            # radix_sort(novoVetor)
            novoVetor, comparacoes, trocas, tempo = timeit.timeit(radix_sort(novoVetor))
            print(f'{novoVetor}\n- Trocas: {trocas}\n- Comparações: {comparacoes}\n- Tempo de resposta: {tempo}')
        case 8:
            pass
        case _:
            pass
