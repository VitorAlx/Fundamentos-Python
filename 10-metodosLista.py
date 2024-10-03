nomeCarros = ["Corsa","Corolla","Strada","Van","Hb20"]

#verificar o tamanho da lista
print(len(nomeCarros))

#obter a posição na lista pelo nome
print(nomeCarros.index("Corsa"))

#adicionar um elemento na última posição da lista
nomeCarros.append("Supra")
print(nomeCarros)

#ordenar uma listar por orde alfabética
nomeCarros.sort()
print(nomeCarros)

#copiar conteúdo de uma lista para outra
nomeCarrosCopy = nomeCarros.copy()

#remover algo da lista
nomeCarrosCopy.remove("Corsa")
print(nomeCarrosCopy)

#remover todos os itens da lista 
nomeCarros.clear()
print(nomeCarros)