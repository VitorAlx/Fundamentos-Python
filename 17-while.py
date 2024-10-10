carList = ["Corolla",  "Corsa", "Van", "Strada", "Hb20"]

# #utilizando while para iterar sobre cada item de uma lista
# index = 0
# while index < len(carList):
#     print(carList[index])
#     index += 1

# #utilizando break, que encerra a estrutura em que está incluso
# index = 0
# while index < len(carList):
#     if carList[index] == "Strada":
#         break
#     print(carList[index])
#     index += 1

# #utilizando continue, que pula para a próxima iteração quando a condição é atendida
# index = 0
# while index < len(carList):
#     if carList[index] == "Strada":
#         index += 1
#         continue
#     print(carList[index])
#     index += 1

#exemplo mais completo

nomeCar = input("Informe o nome do carro: \n")
quantCar = int(input("Informe a quantidade de avaliações: \n"))

total = 0
count = 0

while count < quantCar:
    note = float(input("Informe a nota: \n"))
    total += note
    count += 1

if quantCar > 0:
    media = total / quantCar
else:
     media = 0

print(f"A media das avaliações do carro: {nomeCar} é: {media:.2f}")