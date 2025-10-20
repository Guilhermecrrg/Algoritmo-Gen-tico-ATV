def lerMatrizCidades(arquivo_path="../dados.txt"):
    matriz = []

    with open(arquivo_path, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

        # Ignora a primeira linha (cabeçalho com nomes das cidades)
        for linha in linhas[1:]:
            # Remove espaços extras e quebra de linha
            linha = linha.strip()

            # Remove o texto "Cidade X," do início
            # e mantém apenas os números separados por vírgula
            partes = linha.split(",")
            partes = [p.strip() for p in partes if p.strip() != ""]

            # Ignora o primeiro elemento (ex: "Cidade 1")
            distancias = []
            for item in partes[1:]:
                try:
                    distancias.append(int(item))
                except ValueError:
                    pass  # ignora se não for número
            matriz.append(distancias)

    return matriz


