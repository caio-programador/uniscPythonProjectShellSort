def bubble_sort(vetor):
    n = len(vetor)
    comparacoes = 0
    num_troca = 0
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
    h = len(vetor) // 2
    comparacoes = 0
    num_troca = 0
    while h > 0:

        for startposition in range(h):
            num_troca, comparacoes = gapInsertionSort(vetor, startposition, h, comparacoes, num_troca)

        h = h // 2

    return vetor, comparacoes, num_troca


def gapInsertionSort(alist, start, gap, comparacoes, num_troca):
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        comparacoes += 1

        while position >= gap and alist[position - gap] > currentvalue:
            num_troca += 1
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue
    return num_troca, comparacoes


#  ele pega os menores valores e vai pondo nas menores posicoes
#  faz pesquisa sequencial para achar os menores valores
def selection_sort(vetor):
    pass


def radix_sort(vetor):
    comparacoes, trocas = 0, 0
    return vetor, comparacoes, trocas

#  def PROXIMO_sort(vetor):D

# 8==================D
# essa é das cuiuda
# shiiiiiii, easter-egg
