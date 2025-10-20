from config import matrizCidades

def gerarCustoCaminhos(caminhos):
    custoCaminhos = []
    for i in caminhos:
        custoCaminho = 0
        for num, j in enumerate(i[:-1]):
            if matrizCidades[j][i[num+1]] == 0:
                custoCaminho += 9999
            else:
                custoCaminho += matrizCidades[j][i[num+1]]
        custoCaminhos.append(1/(1+custoCaminho))
    return custoCaminhos