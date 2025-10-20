from tools.leitorDeCidades import lerMatrizCidades
from genetico.populacao import gerarPopulacaoInicial
from genetico.cruzamento import crossoverOxDuplo
from genetico.avaliacao import gerarCustoCaminhos
import config

populacaoInicial = 20

matrizCidades = lerMatrizCidades("src/dados.txt")

individuos = gerarPopulacaoInicial(populacaoInicial, len(matrizCidades[1]))

custoCaminhos = gerarCustoCaminhos(individuos)

print(individuos[0][:99])

print('Matriz1 ', individuos[0])
print('Matriz2 ', individuos[1])

filho1, filho2 = crossoverOxDuplo(individuos[0],individuos[1])
print('filho1 ', filho1)
print('filho2 ', filho2)