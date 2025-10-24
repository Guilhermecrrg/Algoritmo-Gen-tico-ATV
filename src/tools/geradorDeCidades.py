import random

def gerarCidades():
    num_cidades = 101  # total de cidades, incluindo a pizzaria

    with open("src/dados.txt", "w", encoding="utf-8") as arquivo:
        # Cabeçalho com os nomes das cidades
        arquivo.write("Cidade da Pizzaria, ")  # primeira cidade especial
        for i in range(1, 101):  # cidades 1 a 100
            arquivo.write(f"Cidade {i}, ")
        arquivo.write("\n")

        # Linhas com distâncias
        for i in range(num_cidades):
            # Nome da cidade da linha
            if i == 0:
                arquivo.write("Cidade da Pizzaria, ")
            else:
                arquivo.write(f"Cidade {i}, ")

            # Distâncias
            for y in range(num_cidades):
                if y == i:
                    distancia = 0
                else:
                    distancia = random.randint(0, 10)

                # Último valor sem vírgula
                if y < num_cidades - 1:
                    arquivo.write(f"{distancia},")
                else:
                    arquivo.write(f"{distancia}")
            arquivo.write("\n")

if __name__ == "__main__":
    gerarCidades()
