import random

def gerarPopulacaoInicial(tamanhoPopulacao, numCidades):

    listaCidades = list(range(numCidades))  # Ex: [0, 1, 2, ..., 99]
    populacao = []

    for _ in range(tamanhoPopulacao):
        individuo = listaCidades.copy()
        random.shuffle(individuo)  # embaralha as cidades para criar rota aleatória
        populacao.append(individuo)

    return populacao


if __name__ == "__main__":
    populacao = gerarPopulacaoInicial(tamanhoPopulacao=5, numCidades=10)
    for i, individuo in enumerate(populacao):
        print(f"Indivíduo {i+1}: {individuo}")
