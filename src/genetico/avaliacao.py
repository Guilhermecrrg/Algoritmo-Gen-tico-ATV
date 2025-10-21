import config
import random

def gerarCustoCaminhos(caminhos):
    custoCaminhos = []
    for i in caminhos:
        custoCaminho = 0
        for num, j in enumerate(i[:-1]):
            if config.matrizCidades[j][i[num+1]] == 0:
                custoCaminho += 9999
            else:
                custoCaminho += config.matrizCidades[j][i[num+1]]
        custoCaminhos.append(1/(1+custoCaminho))
    return custoCaminhos


def torneio(custos, tamanho_torneio=3):
    
    def selecionar_um():

        competidores = random.sample(range(len(custos)), tamanho_torneio)
        return max(competidores, key=lambda i: custos[i])

    pai1 = selecionar_um()
    pai2 = selecionar_um()

    # Garante que não sejam o mesmo indivíduo
    while pai2 == pai1:
        pai2 = selecionar_um()

    return pai1, pai2