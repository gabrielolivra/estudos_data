####################### LENDO ARQUIVOS ########################


dados = []
lista_idades = []
with open(file='banco.csv', mode='r', encoding="utf-8") as arquivo:
    linha = arquivo.readline()
    while linha:
        linha = arquivo.readline()
        dados.append(linha)   
    for i in dados:
        if i != '':
            lista_dados = i.split(sep=",")
            id = int(lista_dados[0])
            nome = lista_dados[1]
            idade = lista_dados[2]
            cidade = lista_dados[3]
            lista_idades.append({"id":id,"nome":nome, "idade":idade, "cidade": cidade})


################# ESCREVENDO ARQUIVOS ##########################


with open(file='idades.csv', mode='w', encoding='utf-8') as arquivo:
    linha = 'id,'+'nome,' +'idade,'+'cidade'+'\n'
    arquivo.write(linha)
    for i in lista_idades:
        linha = f"{i['id']},{i['nome']},{i['idade']},{i['cidade']}"
        arquivo.write(linha)
    