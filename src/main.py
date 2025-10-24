from tools.leitorDeCidades import lerMatrizCidades
from genetico.populacao import gerarPopulacaoInicial, elitismo
from genetico.cruzamento import crossoverOxDuplo, mutacao
from genetico.avaliacao import gerarCustoCaminhos, torneio

import config
import time
import matplotlib.pyplot as plt
import csv
from datetime import datetime

inicio_execucao = time.time()

# ==========================
# CONFIGURAÇÕES DO ALGORITMO
# ==========================
NUM_GERACOES = config.numMaxGeracoes
TAXA_MUTACAO = config.taxaMutacao
TAM_POP = config.tamPopulacaoInicial
NUM_ELITISMO = config.numElitismo

# ==========================
# INICIALIZAÇÃO
# ==========================
config.matrizCidades = lerMatrizCidades("src/dados.txt")
config.individuos = gerarPopulacaoInicial(TAM_POP, len(config.matrizCidades))

print("População inicial gerada com", TAM_POP, "indivíduos e", len(config.matrizCidades), "cidades.\n")

# ==========================
# LISTAS PARA GRÁFICOS
# ==========================
geracoes = []
melhores = []
piores = []
medios = []

# ==========================
# LOOP EVOLUTIVO
# ==========================
for geracao in range(NUM_GERACOES):
    custoCaminhos = gerarCustoCaminhos(config.individuos)

    # Calcula métricas da geração
    piorCusto = min(custoCaminhos)
    melhorCusto = max(custoCaminhos)
    mediaCusto = sum(custoCaminhos) / len(custoCaminhos)

    melhorIndice = custoCaminhos.index(melhorCusto)
    melhorIndividuo = config.individuos[melhorIndice]

    # Armazena dados para gráfico
    geracoes.append(geracao + 1)
    melhores.append(melhorCusto)
    piores.append(piorCusto)
    medios.append(mediaCusto)

    print(f"Geração {geracao + 1}/{NUM_GERACOES} | Melhor: {melhorCusto:.5f} | Médio: {mediaCusto:.5f} | Pior: {piorCusto:.5f}")

    # Critério de parada opcional (exemplo)
    # if melhorCusto > 0.9:
    #     break

    # Gera nova população por cruzamento
    novaPopulacao = elitismo(custoCaminhos, NUM_ELITISMO)

    while len(novaPopulacao) < TAM_POP:
        pos1, pos2 = torneio(custoCaminhos)
        pai1, pai2 = config.individuos[pos1], config.individuos[pos2]

        filho1, filho2 = crossoverOxDuplo(pai1, pai2)
        novaPopulacao.extend([filho1, filho2])

    # Atualiza população
    config.individuos = novaPopulacao[:TAM_POP]

    # Aplica mutação
    mutacao(taxaMutacao=TAXA_MUTACAO)

# ==========================
# RESULTADO FINAL
# ==========================
custoFinal = gerarCustoCaminhos(config.individuos)
melhorCustoFinal = max(custoFinal)
melhorIndividuoFinal = config.individuos[custoFinal.index(melhorCustoFinal)]

fim_execucao = time.time()
tempo_execucao = round(fim_execucao - inicio_execucao, 3) 

print("\n=== RESULTADO FINAL ===")
print(f"Melhor custo: {melhorCustoFinal:.5f}")
print("Melhor rota:", melhorIndividuoFinal)

# === SALVAR EM CSV ===

# Nome do arquivo
arquivo_csv = "melhores_rotas.csv"

# Cabeçalhos das colunas
cabecalhos = [
    "DataHora",
    "MelhorCusto",
    "MelhorRota",
    "TempoExecucao_s",
    "tamPopulacaoInicial",
    "taxaMutacao",
    "numMaxGeracoes",
    "numElitismo"
]

# Cria (ou adiciona) os dados no arquivo
with open(arquivo_csv, mode="a", newline="", encoding="utf-8") as arquivo:
    writer = csv.DictWriter(arquivo, fieldnames=cabecalhos)

    # Se o arquivo estiver vazio, escreve o cabeçalho
    if arquivo.tell() == 0:
        writer.writeheader()

    # Monta o dicionário de dados
    linha = {
        "DataHora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "MelhorCusto": round(melhorCustoFinal, 5),
        "MelhorRota": " -> ".join(map(str, melhorIndividuoFinal)),
        "TempoExecucao_s": tempo_execucao,
        "tamPopulacaoInicial": config.tamPopulacaoInicial,
        "taxaMutacao": config.taxaMutacao,
        "numMaxGeracoes": config.numMaxGeracoes,
        "numElitismo": config.numElitismo
    }

    # Escreve a linha no CSV
    writer.writerow(linha)

print(f"\nRota salva em '{arquivo_csv}' com sucesso.")

# ==========================
# GRÁFICO DE CONVERGÊNCIA
# ==========================
plt.figure(figsize=(10, 6))
plt.title("Convergência do Algoritmo Genético", fontsize=14, fontweight="bold")
plt.plot(geracoes, melhores, label="Melhor", color='green', linewidth=2)
plt.plot(geracoes, medios, label="Médio", color='blue', linestyle='--', linewidth=1.5)
plt.plot(geracoes, piores, label="Pior", color='red', linestyle=':', linewidth=1.5)
plt.xlabel("Geração", fontsize=12)
plt.ylabel("Custo do Caminho", fontsize=12)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
