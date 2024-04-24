import numpy as np


def bubble_sort(vetor):
    n = len(vetor)
    comparacoes, num_troca = 0, 0
    troca = True
    while troca:
        troca = False
        for i in range(n - 1):
            comparacoes += 1
            if vetor[i] > vetor[i + 1]:
                vetor[i], vetor[i + 1] = vetor[i + 1], vetor[i]
                troca = True
                num_troca += 1
        n -= 1
    return vetor, comparacoes, num_troca


def insertion_sort(vetor):
    n = len(vetor)
    comparacoes, num_troca = 0, 0
    for index in range(1, n):
        currentValue = vetor[index]
        position = index
        comparacoes += 1
        while position > 0 and vetor[position - 1] > currentValue:
            vetor[position] = vetor[position - 1]
            position -= 1  # Ajuste aqui
            num_troca += 1
        vetor[position] = currentValue
    return vetor, comparacoes, num_troca


def quick_sort(vetor):
    global comparacoes, num_troca
    comparacoes, num_troca = 0, 0
    quick_sort_helper(vetor, 0, len(vetor) - 1)

    return vetor, comparacoes, num_troca


def quick_sort_helper(vetor, first, last):
    global num_comparacoes, num_troca
    if first < last:
        splitpoint = partition(vetor, first, last)

        quick_sort_helper(vetor, first, splitpoint - 1)
        quick_sort_helper(vetor, splitpoint + 1, last)


def partition(vetor, first, last):
    global comparacoes, num_troca
    pivo = vetor[first]

    esquerda = first + 1
    direita = last

    done = False
    while not done:

        comparacoes += 1
        while esquerda <= direita and vetor[esquerda] <= pivo:
            esquerda = esquerda + 1
            comparacoes += 1
        comparacoes += 1
        while vetor[direita] >= pivo and direita >= esquerda:
            direita = direita - 1
            comparacoes += 1

        if direita < esquerda:
            done = True
        else:
            temp = vetor[esquerda]
            vetor[esquerda] = vetor[direita]
            vetor[direita] = temp
            num_troca += 1

    temp = vetor[first]
    vetor[first] = vetor[direita]
    vetor[direita] = temp

    return direita


def merge_sort(vetor):
    global comparacoes, num_troca
    num_troca, comparacoes = 0, 0
    vetor = merge_sort_helper(vetor)
    return vetor, comparacoes, num_troca


def merge_sort_helper(vetor):
    global comparacoes, num_troca
    if len(vetor) <= 1:
        return vetor

    meio = len(vetor) // 2

    esquerda = merge_sort_helper(vetor[:meio])
    direita = merge_sort_helper(vetor[meio:])

    return merge(esquerda, direita)


def merge(esquerda, direita):
    global comparacoes, num_troca
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        comparacoes += 1
        if esquerda[i] < direita[j]:
            num_troca += 1
            resultado.append(esquerda[i])
            i += 1
        else:
            num_troca += 1
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return np.array(resultado)


def shell_sort(vetor):
    global comparacoes, num_troca
    h = len(vetor) // 2
    comparacoes = 0
    num_troca = 0
    while h > 0:

        for startposition in range(h):
            gapInsertionSort(vetor, startposition, h)

        h = h // 2

    return vetor, comparacoes, num_troca


def gapInsertionSort(vetor, start, h):
    global comparacoes, num_troca
    for i in range(start + h, len(vetor), h):
        currentvalue = vetor[i]
        position = i
        comparacoes += 1

        while position >= h and vetor[position - h] > currentvalue:
            num_troca += 1
            vetor[position] = vetor[position - h]
            position = position - h

        vetor[position] = currentvalue


def selection_sort(vetor):
    n = len(vetor)
    comparacoes, num_troca = 0, 0

    for i in range(n):
        min = i
        for j in range(i + 1, n):
            comparacoes += 1
            if vetor[j] < vetor[min]:
                min = j

        if min != i:
            vetor[i], vetor[min] = vetor[min], vetor[i]
            num_troca += 1

    return vetor, comparacoes, num_troca


def counting_sort(vetor, place):
    global comparacoes, num_troca
    size = len(vetor)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        comparacoes += 1
        index = vetor[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = vetor[i] // place
        output[count[index % 10] - 1] = vetor[i]
        count[index % 10] -= 1
        num_troca += 1
        i -= 1

    for i in range(0, size):
        vetor[i] = output[i]
        num_troca += 1


def radix_sort(vetor):
    global comparacoes, num_troca
    comparacoes, num_troca = 0, 0
    # Get maximum element
    max_element = max(vetor)

    place = 1
    while max_element // place > 0:
        counting_sort(vetor, place)
        place *= 10

    return vetor, comparacoes, num_troca


def insertion_sort_bucket(arr):
    comparacoes = 0
    num_troca = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            comparacoes += 1
            num_troca += 1
        arr[j + 1] = key
        num_troca += 1
    return comparacoes, num_troca


def bucket_sort(vetor):
    n = len(vetor)
    baldes = [[] for _ in range(n)]

    for num in vetor:
        index = min(int(num * n), n - 1)  # Limita o índice dentro dos limites aceitáveis
        baldes[index].append(num)

    comparacoes = 0
    num_troca = 0

    for i in range(n):
        comp, swap = insertion_sort_bucket(baldes[i])
        comparacoes += comp
        num_troca += swap

    k = 0
    for i in range(n):
        for num in baldes[i]:
            vetor[k] = num
            k += 1
    return vetor, num_troca, comparacoes
