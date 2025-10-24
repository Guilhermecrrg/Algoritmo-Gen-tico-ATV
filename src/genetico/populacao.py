import random
import time

def gerarPopulacaoInicial(tamanhoPopulacao, numCidades):

    listaCidades = list(range(numCidades))
    populacao = []

    for _ in range(tamanhoPopulacao):
        individuo = listaCidades.copy()
        random.shuffle(individuo) 
        populacao.append(individuo)

    return populacao
