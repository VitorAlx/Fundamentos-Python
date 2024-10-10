#carList = ["Corolla",  "Corsa", "Van", "Strada", "Hb20"]

# #iterando com o for na lista
# for car in carList:
#     print(car)

# #utilizando break, que encerra a estrutura em que está incluso
# for car in carList:
#     if car == "Strada":
#         break
#     print(car)

# #utilizando continue, que pula para a próxima iteração quando a condição é atendida
# for car in carList:
#     if car == "Strada":
#         continue
#     print(car)

#exemplo mais completo
listaCar = {}
total = 0

quantCar = int(input("Informe a quantidade de carros que deseja incluir: \n"))

if quantCar > 0:
    for i in range(quantCar):
        nomeCar = input("Informe o nome do carro: \n")

        if nomeCar == "0":
            continue

        notaCar = float(input("Informe a nota do carro: \n"))

        if notaCar == 0:
            continue

        listaCar[nomeCar] = notaCar

        total += notaCar

        if nomeCar == "" or notaCar is None:
            break

    for car, nota in listaCar.items():
        print(f"{car}: {nota}\n")

    if total != 0:
        media = total / quantCar

    else:
        exit()

    print(f"A nota media dos {quantCar} carros foi: {media:.2f}\n")
    
else:
    exit()
