from tools.leitorDeCidades import lerMatrizCidades
from genetico.populacao import gerarPopulacaoInicial

populacaoInicial = 20

matrizCidades = lerMatrizCidades("src/dados.txt")

matriz = gerarPopulacaoInicial(populacaoInicial, len(matrizCidades[1]))
print(matriz[0][:99])
