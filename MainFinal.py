# BIBLIOTECAS
import sys
import numpy as np
from numpy import random as rd
from utils.Utils import *


limpa_arquivo()
arquivo = "Casos de teste"
sys.setrecursionlimit(10000000)
for i in range(1, 4):
    print(f"CENÁRIO {i}:\n\n")
    adicionar_texto(arquivo, f"CENÁRIO {i}\n\n")
    adicionar_texto(arquivo, "PEQUENO - 1000 DADOS\n\n")
    vetorPequenoAleatorio = rd.randint(1, 10000, 1000)
    print("PEQUENO - 1000 DADOS")
    test(vetorPequenoAleatorio)

    adicionar_texto(arquivo, "MÉDIO - 10000 DADOS\n\n")
    vetorMedioAleatorio = rd.randint(1, 100000, 10000)
    print("MÉDIO - 10000 DADOS")
    test(vetorMedioAleatorio)

    adicionar_texto(arquivo, "GRANDE - 50000 DADOS\n\n")
    vetorGrandeAleatorio = rd.randint(1, 500000, 50000)
    print("GRANDE - 50000 DADOS")
    test(vetorGrandeAleatorio)

    adicionar_texto(arquivo, "SUPER GRANDE - 100000 DADOS\n\n")
    vetorSuperGrandeAleatorio = rd.randint(1, 1000000, 100000)
    print("SUPER GRANDE - 100000 DADOS")
    test(vetorSuperGrandeAleatorio)
    print()


