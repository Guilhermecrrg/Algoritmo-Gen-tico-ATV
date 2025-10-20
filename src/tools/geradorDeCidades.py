import random

def gerarCidades():
    with open("dados.txt", "w", encoding="utf-8") as arquivo:
        # Cabeçalho com os nomes das cidades
        for i in range(100):
            arquivo.write(f"Cidade {i + 1}, ")
        arquivo.write("\n")

        # Linhas com distâncias
        for i in range(100):
            arquivo.write(f"Cidade {i + 1}, ")
            for y in range(100):
                if y == i:
                    distancia = 0
                else:
                    distancia = random.randint(0, 10)

                # Último valor sem vírgula no final da linha
                if y < 99:
                    arquivo.write(f"{distancia},")
                else:
                    arquivo.write(f"{distancia}")
            arquivo.write("\n")

if __name__ == "__main__":
    gerarCidades()
