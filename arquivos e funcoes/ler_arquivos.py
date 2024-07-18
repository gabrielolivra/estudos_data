# ler arquivos

#metodos

# Leitura (r): Abre o arquivo para leitura. Esse é o modo padrão.

# Escrita (w): Abre o arquivo para escrita. Se o arquivo já existir, seu conteúdo será truncado.

# Acrescentar (a): Abre o arquivo para escrita, mas adiciona os dados ao final do arquivo existente, sem truncar.

# Leitura e escrita (r+): Abre o arquivo para leitura e escrita.

# Escrita e leitura (w+): Abre o arquivo para leitura e escrita, truncando o arquivo existente.

# Acrescentar e leitura (a+): Abre o arquivo para leitura e escrita, adicionando dados ao final do arquivo existente.
dados = []
with open(file='banco.csv', mode='r', encoding="utf-8") as arquivo:
    linha = arquivo.readline()
    while linha:
        linha = arquivo.readline()
        dados.append(linha)
    list_id = []   
    for i in dados:
        if i != '':
            lista_dados = i.split(sep=",")
            id = int(lista_dados[0])
            nome = lista_dados[1]
            idade = lista_dados[2]
            cidade = lista_dados[3]
            list_id.append(id)
    print(list_id)
        