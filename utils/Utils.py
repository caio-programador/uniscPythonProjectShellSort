from time import time
import timeit

from Sort.Sort import *


def all_sort(sort_type, vetor):
    novoVetor = vetor.copy()

    match sort_type:
        case 1:
            print("\nBUBBLE SORT")
            inicio = time()
            novoVetor, comparacoes, trocas = bubble_sort(novoVetor)
            total = time() - inicio
            print(f'\n- Trocas: {trocas}\n- Comparações: {comparacoes}\n- Tempo de resposta: {total}')
            criar_arquivo(total, trocas, comparacoes, sort_type)
        case 2:
            print("\nSHELL SORT")
            inicio = time()
            novoVetor, comparacoes, trocas = shell_sort(novoVetor)
            total = time() - inicio
            print(f'\n- Trocas: {trocas}\n- Comparações: {comparacoes}\n- Tempo de resposta: {total}')
            criar_arquivo(total, trocas, comparacoes, sort_type)
        case 3:
            print("\nQUICK SORT")
            inicio = time()
            novoVetor, comparacoes, trocas = quick_sort(novoVetor)
            total = time() - inicio
            print(f'\n- Trocas: {trocas}\n- Comparações: {comparacoes}\n- Tempo de resposta: {total}')
            criar_arquivo(total, trocas, comparacoes, sort_type)
        case 4:
            print("\nINSERTION SORT")
            inicio = time()
            novoVetor, comparacoes, trocas = insertion_sort(novoVetor)
            total = time() - inicio
            print(f'\n- Trocas: {trocas}\n- Comparações: {comparacoes}\n- Tempo de resposta: {total}')
            criar_arquivo(total, trocas, comparacoes, sort_type)
        case 5:
            inicio = time()
            print("\nMERGE SORT")
            inicio = time()
            novoVetor, comparacoes, trocas = merge_sort(novoVetor)
            total = time() - inicio
            print(f'\n- Trocas: {trocas}\n- Comparações: {comparacoes}\n- Tempo de resposta: {total}')
            criar_arquivo(total, trocas, comparacoes, sort_type)
        case 6:
            inicio = time()
            print("\nSELECTION SORT")
            inicio = time()
            novoVetor, comparacoes, trocas = selection_sort(novoVetor)
            total = time() - inicio
            print(f'\n- Trocas: {trocas}\n- Comparações: {comparacoes}\n- Tempo de resposta: {total}')
            criar_arquivo(total, trocas, comparacoes, sort_type)
        case 7:
            inicio = time()
            print("\nRADIX SORT")
            inicio = time()
            novoVetor, comparacoes, trocas = radix_sort(novoVetor)
            total = time() - inicio
            print(f'\n- Trocas: {trocas}\n- Comparações: {comparacoes}\n- Tempo de resposta: {total}')
            criar_arquivo(total, trocas, comparacoes, sort_type)
        case 8:
            inicio = time()
            print("\nBUCKET SORT")
            inicio = time()
            novoVetor, comparacoes, trocas = bucket_sort(novoVetor)
            total = time() - inicio
            print(f'\n- Trocas: {trocas}\n- Comparações: {comparacoes}\n- Tempo de resposta: {total}')
            criar_arquivo(total, trocas, comparacoes, sort_type)
        case _:
            pass


def test(vetor):
    for i in range(9):
        all_sort(i, vetor)


def criar_arquivo(total, trocas, comparacoes, sort_type):
    sorts = ["BUBBLE SORT", "SHELL SORT", "QUICK SORT", "INSERTION SORT", "MERGE SORT",
             "SELECTION SORT", "RADIX SORT", "BUCKET SORT"]
    with open("Casos de teste", 'a') as arquivo:
        arquivo.write(f'Tipo de ordenação: {sorts[sort_type-1]}\n')
        arquivo.write(f'Trocas: {trocas}\n')
        arquivo.write(f'Comparações: {comparacoes}\n')
        arquivo.write(f'Tempo total de execução: {total:,.10f} segundos\n')
        arquivo.write("\n")


def limpa_arquivo():
    with open("Casos de teste", "w") as arquivo:
        arquivo.truncate(0)


def adicionar_texto(a, texto):
    with open(a, 'a') as arquivo:
        arquivo.write(texto)