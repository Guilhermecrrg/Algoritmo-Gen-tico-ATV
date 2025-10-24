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


def mutacao(taxaMutacao):
    for i in range(len(config.individuos)):
        for j in range(len(config.individuos[i])):
            r_muta = random.random()
            if r_muta < taxaMutacao:
                # Escolhe outra posição aleatória diferente de j
                k = random.randint(0, len(config.individuos[i]) - 1)
                while k == j:
                    k = random.randint(0, len(config.individuos[i]) - 1)

                # Troca as cidades de posição (swap)
                config.individuos[i][j], config.individuos[i][k] = config.individuos[i][k], config.individuos[i][j]


def crossoverOxDuplo(pai1, pai2):
    n = len(pai1)
    corte1, corte2 = sorted(random.sample(range(n), 2))

    def gerarFilho(paiA, paiB):
        filho = [None] * n
        filho[corte1:corte2] = paiA[corte1:corte2]
        pos = corte2
        for cidade in paiB:
            if cidade not in filho:
                if pos >= n:
                    pos = 0
                filho[pos] = cidade
                pos += 1
        return filho

    filho1 = gerarFilho(pai1, pai2)
    filho2 = gerarFilho(pai2, pai1)

    return filho1, filho2
