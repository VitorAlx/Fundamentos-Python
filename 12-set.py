#obs: no set o valor true e o valor 1 são considerados o mesmo
nomeCarros = {"Corsa","Corolla","Strada","Van","Hb20"}
nomeCarros2 = {"Marea", "Uno", "Fusca", "Combi"}

#verificar o tamanho do set
print(len(nomeCarros))

#adicionar um set a outro set
nomeCarros.update(nomeCarros2)
print(nomeCarros)

#remover itens do set
nomeCarros.remove("Marea")
nomeCarros.remove("Uno")
print(nomeCarros)