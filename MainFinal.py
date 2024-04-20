import sys

import numpy as np
from numpy import random as rd
from utils.Utils import test

sys.setrecursionlimit(10000000)

vetorPequenoAleatorio = rd.randint(1, 10000, 1000)
vetorPequenoDecrescente = np.sort(vetorPequenoAleatorio)[::-1]
vetorPequenoUnico = [100] * 1000
print("PEQUENO - 1000 DADOS\n")
print("\nCenário 1 - Vetor com elementos aleatórios")
test(vetorPequenoAleatorio)

print("\nCenário 2 - Vetor com elementos aleatórios em ordem decrescente")
test(vetorPequenoDecrescente)

print("\nCenário 3 - Vetor com elementos iguais")
test(vetorPequenoUnico)


vetorMedioAleatorio = rd.randint(1, 100000, 10000)
vetorMedioDecrescente = np.sort(vetorMedioAleatorio)[::-1]
vetorMedioUnico = [100] * 10000

print("\nMÉDIO - 10000 DADOS\n")
print("\nCenário 1 - Vetor com elementos aleatórios")
test(vetorMedioAleatorio)

print("\nCenário 2 - Vetor com elementos aleatórios em ordem decrescente")
test(vetorMedioDecrescente)

print("\nCenário 3 - Vetor com elementos iguais")
test(vetorMedioUnico)

vetorGrandeAleatorio = rd.randint(1, 500000, 50000)
vetorGrandeDecrescente = np.sort(vetorGrandeAleatorio)[::-1]
vetorGrandeUnico = [100] * 50000
print("\nGRANDE - 50000 DADOS\n")

print("\nCenário 1 - Vetor com elementos aleatórios")
test(vetorGrandeAleatorio)

print("\nCenário 2 - Vetor com elementos aleatórios em ordem decrescente")
test(vetorGrandeDecrescente)

print("\nCenário 3 - Vetor com elementos iguais")
test(vetorGrandeUnico)

vetorSuperGrandeAleatorio = rd.randint(1, 1000000, 100000)
vetorSuperGrandeDecrescente = np.sort(vetorSuperGrandeAleatorio)[::-1]
vetorSuperGrandeUnico = [100] * 100000

print("\nSUPER GRANDE - 100000 DADOS\n")

print("\nCenário 1 - Vetor com elementos aleatórios")
test(vetorSuperGrandeAleatorio)

print("\nCenário 2 - Vetor com elementos aleatórios em ordem decrescente")
test(vetorSuperGrandeDecrescente)

print("\nCenário 3 - Vetor com elementos iguais")
test(vetorSuperGrandeUnico)
