from tools.leitorDeCidades import lerMatrizCidades
from genetico.populacao import gerarPopulacaoInicial
from genetico.cruzamento import crossoverOxDuplo
import config

def gerarCustoCaminhos(caminhos):
    custoCaminhos = []
    for i in caminhos:
        custoCaminho = 0
        for num, j in enumerate(i[:-1]):
            custoCaminho += matrizCidades[j][i[num+1]]
        custoCaminhos.append(custoCaminho)
    return custoCaminhos

populacaoInicial = 20

matrizCidades = lerMatrizCidades("src/dados.txt")

print(matrizCidades)

caminhos = gerarPopulacaoInicial(populacaoInicial, len(matrizCidades[1]))

custoCaminhos = gerarCustoCaminhos(caminhos)

print(caminhos[0][:99])

print('Matriz1 ', caminhos[0])
print('Matriz2 ', caminhos[1])

filho1, filho2 = crossoverOxDuplo(caminhos[0],caminhos[1])
print('filho1 ', filho1)
print('filho2 ', filho2)