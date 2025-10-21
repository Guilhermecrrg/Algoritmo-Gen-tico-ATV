from tools.leitorDeCidades import lerMatrizCidades
from genetico.populacao import gerarPopulacaoInicial
from genetico.cruzamento import crossoverOxDuplo
from genetico.avaliacao import gerarCustoCaminhos,torneio
import config


config.matrizCidades = lerMatrizCidades("src/dados.txt")
print(config.matrizCidades)
individuos = gerarPopulacaoInicial(config.tamPopulacaoInicial, len(config.matrizCidades))

custoCaminhos = gerarCustoCaminhos(individuos)
#print(custoCaminhos)

pos1, pos2 = torneio(custoCaminhos)

# print(individuos[0][:99])

print('Matriz1 ', individuos[pos1])
print('Matriz2 ', individuos[pos2])

filho1, filho2 = crossoverOxDuplo(individuos[pos1],individuos[pos2])
print('filho1 ', filho1)
print('filho2 ', filho2)

print(len(config.matrizCidades))