import random

def gerarPopulacaoInicial(tamanhoPopulacao, numCidades):

    listaCidades = list(range(numCidades))
    populacao = []

    for _ in range(tamanhoPopulacao):
        individuo = listaCidades.copy()
        random.shuffle(individuo) 
        populacao.append(individuo)

    return populacao


if __name__ == "__main__":
    populacao = gerarPopulacaoInicial(tamanhoPopulacao=5, numCidades=10)
    for i, individuo in enumerate(populacao):
        print(f"Indivíduo {i+1}: {individuo}")
