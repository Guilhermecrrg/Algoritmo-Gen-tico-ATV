import random
import config

def validarCaminho(cidade1: int, cidade2: int) -> bool:
    if config.matrizCidades is None:
        raise ValueError("A matriz de cidades ainda não foi carregada em config.matrizCidades.")

    if cidade1 < 0 or cidade2 < 0 or \
       cidade1 >= len(config.matrizCidades) or cidade2 >= len(config.matrizCidades):
        raise IndexError(f"Cidades inválidas: {cidade1}, {cidade2}")

    distancia = config.matrizCidades[cidade1][cidade2]
    return distancia > 0


def caminhoValido(rota: list) -> bool:
    for i in range(len(rota) - 1):
        if not validarCaminho(rota[i], rota[i + 1]):
            return False
    return True


def mutacao(taxaMutacao, num_swaps=3):
    for i in range(len(config.individuos)):
        if random.random() < taxaMutacao:
            for _ in range(num_swaps):
                j, k = random.sample(range(1, len(config.individuos[i])), 2)
                # swap
                config.individuos[i][j], config.individuos[i][k] = config.individuos[i][k], config.individuos[i][j]


def crossoverOxDuplo(pai1, pai2):
    n = len(pai1)
    corte1, corte2 = sorted(random.sample(range(1, n), 2))

    def gerarFilho(paiA, paiB):
        filho = [None] * n
        filho[0] = 0
        filho[corte1:corte2] = paiA[corte1:corte2]
        pos = corte2
        for cidade in paiB:
            if cidade not in filho:
                if pos >= n:
                    pos = 1
                filho[pos] = cidade
                pos += 1
        return filho

    filho1 = gerarFilho(pai1, pai2)
    filho2 = gerarFilho(pai2, pai1)

    return filho1, filho2
