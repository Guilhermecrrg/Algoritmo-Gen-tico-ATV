import random

def gerarPopulacaoInicial(tamanhoPopulacao, numCidades):

    listaCidades = list(range(numCidades))
    populacao = []

    for _ in range(tamanhoPopulacao):
        individuo = listaCidades.copy()
        random.shuffle(individuo) 
        populacao.append(individuo)

    return populacao

# ARRUMAR CARAIO


def evoluir(populacao, C, max_geracoes=MAX_GENERATIONS):
    tempo_inicial = time.time()
    melhor_aptidao = -1
    geracoes_sem_melhora = 0
    melhor_solucao = None

    for geracao in range(max_geracoes):
        # Avaliar população
        aptidoes = avaliar_populacao(populacao, C)

        # Verificar se a aptidão mínima foi atingida
        if max(aptidoes) >= APTIDAO_MINIMA:
            print(f"Aptidão mínima atingida: {max(aptidoes)} na geração {geracao}")
            break

        # Seleção e crossover
        nova_populacao = []
        while len(nova_populacao) < POP_SIZE:
            pai1 = torneio_selecao(populacao)
            pai2 = torneio_selecao(populacao)
            filho = crossover(pai1, pai2)
            if random.random() < 0.1:  # Probabilidade de mutação
                mutacao(filho)
            nova_populacao.append(filho)

        # Substituir a população antiga pela nova
        populacao = nova_populacao

        # Verificar se houve melhoria
        melhor_atual = max(aptidoes)
        if melhor_atual > melhor_aptidao:
            melhor_aptidao = melhor_atual
            melhor_solucao = populacao[aptidoes.index(melhor_atual)]
            geracoes_sem_melhora = 0
        else:
            geracoes_sem_melhora += 1

        # Verificar critério de geração sem melhoria
        if geracoes_sem_melhora >= MAX_GERACOES_SIN_DIST:
            print(f"Sem melhoria significativa por {MAX_GERACOES_SIN_DIST} gerações. Parando...")
            break

        # Verificar tempo de execução
        if time.time() - tempo_inicial > MAX_TEMPO_EXECUCAO:
            print("Tempo máximo de execução atingido.")
            break

        # Imprimir progresso
        if geracao % 100 == 0:
            print(f"Geração {geracao}: Melhor aptidão = {melhor_aptidao}")

    return melhor_solucao, melhor_aptidao

# Exemplo de uso
# populacao_inicial = [random.sample(range(1, N+1), N) for _ in range(POP_SIZE)]  # População inicial aleatória
# melhor_solucao, melhor_aptidao = evoluir(populacao_inicial, C=matrizCidades)

# print(f"Melhor solução encontrada: {melhor_solucao} com aptidão {melhor_aptidao}")