# BIBLIOTECAS
import numpy as np

""""
Bubble Sort: troca elementos adjacentes até que a lista esteja ordenada.
"""
def bubble_sort(vetor):                 # bubble sort "inteligente"
    n = len(vetor)
    comparacoes, num_troca = 0, 0
    troca = True

    while troca:                        # Enquanto troca for verdadeiro, quer dizer que ainda há trocas a fazer
        troca = False
        for i in range(n - 1):          # Percorre o vetor
            comparacoes += 1
            if vetor[i] > vetor[i + 1]: # comparação entre 2 valores
                vetor[i], vetor[i + 1] = vetor[i + 1], vetor[i]
                troca = True            # Informa que ocorreu a troca
                num_troca += 1          # ocorre troca se entrar na condição
        n -= 1                          # tamanho da lista - 1, pois o maior elemento já está em sua posição
    return vetor, comparacoes, num_troca

""""
 Insertion Sort: percorre um vetor da esquerda para a direita, ordenando os elementos à esquerda à medida que avança.
"""
def insertion_sort(vetor):
    n = len(vetor)
    comparacoes, num_troca = 0, 0
    for index in range(1, n):           # Começa no segundo elemento
        currentValue = vetor[index]     # Pega o valor atual
        position = index                # Posicao como do indice atual

        comparacoes += 1
        while position > 0 and vetor[position - 1] > currentValue: # Loop para encontrar a posição correta para inserir o valor atual
            vetor[position] = vetor[position - 1]                  # Elemento maior vai para direita
            position -= 1  # Ajuste aqui
            num_troca += 1
        vetor[position] = currentValue
    return vetor, comparacoes, num_troca

"""
Quick Sort:  divide a lista em torno de um elemento pivô e ordena recursivamente as sublistas resultantes
"""
def quick_sort(vetor):
    global comparacoes, num_troca
    comparacoes, num_troca = 0, 0
    quick_sort_helper(vetor, 0, len(vetor) - 1)

    return vetor, comparacoes, num_troca

"""
Função que faz a recursividade do quick_sort
"""
def quick_sort_helper(vetor, first, last):
    global num_comparacoes, num_troca
    if first < last:
        splitpoint = partition(vetor, first, last)

        quick_sort_helper(vetor, first, splitpoint - 1)
        quick_sort_helper(vetor, splitpoint + 1, last)

"""
Função que cria as partições do quick_sort
"""
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

"""
Merge Sort: divide a lista em metades, ordena cada metade e depois mescla as metades ordenadas.
"""
def merge_sort(vetor):
    global comparacoes, num_troca
    num_troca, comparacoes = 0, 0
    vetor = merge_sort_helper(vetor)
    return vetor, comparacoes, num_troca

"""
Função que faz a recursividade
"""
def merge_sort_helper(vetor):
    global comparacoes, num_troca
    if len(vetor) <= 1:
        return vetor

    meio = len(vetor) // 2

    esquerda = merge_sort_helper(vetor[:meio])
    direita = merge_sort_helper(vetor[meio:])

    return merge(esquerda, direita)

"""
Função responsável por mesclar 
"""
def merge(esquerda, direita):
    global comparacoes, num_troca
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):   # faz a comparação
        comparacoes += 1
        if esquerda[i] < direita[j]:
            num_troca += 1                          # realiza a troca
            resultado.append(esquerda[i])
            i += 1
        else:
            num_troca += 1
            resultado.append(direita[j])           # realiza a troca
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return np.array(resultado)

""""
Shell Sort: divide a lista em subgrupos menores e os ordena independentemente, reduzindo gradualmente a lacuna entre os 
elementos comparados. É um insertion sort aprimorado.
"""
def shell_sort(vetor):
    global comparacoes, num_troca
    h = len(vetor) // 2             # Define o tamanho do intervalo
    comparacoes = 0
    num_troca = 0

    while h > 0:                    # Enquanto o houver um intervalo

        for startposition in range(h):
            gapInsertionSort(vetor, startposition, h)   # chama o insertion sort para cada intervalo

        h = h // 2                 # Reduz o intervalo pela metade

    return vetor, comparacoes, num_troca


"""
Função utilizada pelo shell_sort para separar em subgrupos e realizar a ordenação
"""
def gapInsertionSort(vetor, start, h):
    global comparacoes, num_troca
    for i in range(start + h, len(vetor), h):
        currentvalue = vetor[i]
        position = i

        comparacoes += 1
        while position >= h and vetor[position - h] > currentvalue:     # faz a comparação
            num_troca += 1                                              # se entrar no while faz a troca
            vetor[position] = vetor[position - h]
            position = position - h

        vetor[position] = currentvalue

"""
Selection sort: passar sempre o menor valor do vetor para a primeira posição, depois o segundo menor valor para a 
segunda posição e assim sucessivamente.
"""
def selection_sort(vetor):
    n = len(vetor)                           # pega tamanho do vetor
    comparacoes, num_troca = 0, 0

    for i in range(n):
        min = i                             # Define o indice atual como o menor
        for j in range(i + 1, n):           # Loop para encontrar o índice do menor elemento restante no vetor
            comparacoes += 1
            if vetor[j] < vetor[min]:       # compara o atual com o min. Se atual for menor, ele vira o min
                min = j

        if min != i:                        # Se o menor elemento não estiver na posição atual troca
            vetor[i], vetor[min] = vetor[min], vetor[i]
            num_troca += 1

    return vetor, comparacoes, num_troca



"""
Radix Sort: ordena os elementos processando seus dígitos individuais, em vez de comparar diretamente os valores 
dos elementos.
"""
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


"""
Função utilizada pelo radix_sort para ordenar 
"""
def counting_sort(vetor, place):
    global comparacoes, num_troca
    size = len(vetor)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = vetor[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = vetor[i] // place
        output[count[index % 10] - 1] = vetor[i] # coloca dentro do balde
        num_troca += 1
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        vetor[i] = output[i] # atualiza o vetor original
        num_troca += 1


""""
Bucket Sort: divide a lista em compartimentos, distribui os elementos em cada compartimento com base em seu valor e, 
em seguida, ordena cada compartimento antes de combiná-los para obter a lista ordenada.
"""
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


"""
Função de insertion utilizada pelo bucket_sort
"""
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



