#listando valores de 0 a 10 menores que 4
# listNumbers = [i for i in range(10) if i < 4]
# print(listNumbers)

#trabalhando com a list comprehension
carList = ["Corolla",  "Corsa", "Van", "Strada", "Hb20"]
carListComA = [cars for cars in  carList if 'a' in cars.lower()]
print(carListComA)

#carros que não possuo
carListNot = [cars for cars in carList if cars != "Corsa"]
print(carListNot)

#procurando um filme na lista
while True:
    searchName = input("Digite o nome do carro para buscar na lista (ou sair para encerrar):\n")
    if searchName.lower() == "sair":
        print("Programa Encerrado")
        break
    
    foundMovies = [car for car in carList if searchName.lower() in car.lower()]
    if foundMovies:
        print(f"Carro(s) encontrado(s) com o nome: {searchName}:")
        for foundMovies  in foundMovies:
            print(foundMovies)
    else:
        print(f"Nenhum carro foi encontrado com o nome {searchName}. Tente Novamente!")