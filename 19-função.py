# carList = ["Corolla",  "Corsa", "Van", "Strada", "Hb20"]

# def exibirLista(List):
#     for item in List:
#         print(item)

# exibirLista(carList)

carList = []

def inserirElementosList(carList):
    while True:
        item = input("Informe um elemento para colocar na lista ou 'sair' para fechar: ")
        if item.lower() != "sair":
            carList.append(item)
        else:
            break
    
flag = input("Quer começar o programa de listas e funções? Informe 'Sim' ou 'Não': \n")
if flag.lower() == "sim":
    inserirElementosList(carList)
else:
    exit()

print(carList)