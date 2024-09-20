name = input("Informe o nome do carro: \n")
yearLaunch = int(input("Informe o Ano de lançamento do carro: \n"))
noteCar = float(input("Informe a nota geral do carro: \n"))

# 1° forma:
print("Nome do Carro: ", name, " - Ano de lançamento: ", yearLaunch, " - Nota geral: ", noteCar)

print("__________________________________________________________________________________________")

# 2° forma: f string
print(f"Nome do Carro: {name} - Ano de lançamento: {yearLaunch} - Nota geral: {noteCar}")
