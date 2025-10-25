import random

def gerarCidades():
    num_cidades = 101

    with open("src/dados.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(", ")
        arquivo.write("Cidade da Pizzaria, ")
        for i in range(1, 101):
            arquivo.write(f"Cidade {i}, ")
        arquivo.write("\n")

        for i in range(num_cidades):

            if i == 0:
                arquivo.write("Cidade da Pizzaria, ")
            else:
                arquivo.write(f"Cidade {i}, ")

            for y in range(num_cidades):
                if y == i:
                    distancia = 0
                else:
                    distancia = random.randint(0, 10)

                if y < num_cidades - 1:
                    arquivo.write(f"{distancia},")
                else:
                    arquivo.write(f"{distancia}")
            if i < num_cidades - 1:
                arquivo.write("\n")

if __name__ == "__main__":
    gerarCidades()
