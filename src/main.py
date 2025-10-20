from tools.leitorDeCidades import lerMatrizCidades
from genetico.populacao import gerarPopulacaoInicial
from genetico.cruzamento import crossoverOxDuplo
import config

populacaoInicial = 20

config.matrizCidades = lerMatrizCidades("src/dados.txt")

matriz = gerarPopulacaoInicial(populacaoInicial, len(matrizCidades[1]))
#print(matriz[0][:99])

print('Matriz1 ', matriz[0])
print('Matriz2 ', matriz[1])

filho1, filho2 = crossoverOxDuplo(matriz[0],matriz[1])
print('filho1 ', filho1)
print('filho2 ', filho2)