import random

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
