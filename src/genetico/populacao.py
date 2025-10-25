import random
import config


def gerarPopulacaoInicial(tamanhoPopulacao, numCidades):
    listaCidades = list(range(1, numCidades))
    populacao = []

    for _ in range(tamanhoPopulacao):
        individuo = listaCidades.copy()
        random.shuffle(individuo)
        individuo = [0] + individuo
        populacao.append(individuo)

    return populacao


def elitismo(custoCaminhos, numElitismo):

    novaPopulacao = []

    indicesOrdenados = sorted(range(len(custoCaminhos)), key=lambda i: custoCaminhos[i], reverse=True)
    melhores = [config.individuos[i] for i in indicesOrdenados[:numElitismo]]

    novaPopulacao.extend(melhores)

    return novaPopulacao
