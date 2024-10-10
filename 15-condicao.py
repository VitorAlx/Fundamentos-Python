# modelo = input("Informe o Modelo do carro: \n")
# ano = int(input("Informe o Ano do carro: \n"))
# cor = input("Informe a Cor do carro: \n")
# estadoPintura = bool(input("O estado da pintura do carro é bom? \n"))

# if estadoPintura == "true":
#     if  ano > 2020:
#         print("O carro é novo e a pintura está boa")
#     else:
#         print("O carro é velho más a pintura está boa")
# else:
#     if  ano > 2020:
#         print("O carro é novo más a pintura está ruim")
#     else:
#         print("O carro é velho e a pintura está ruim")

num1 = float(input("Informe o primeiro número: \n"))
num2 = float(input("Informe o segundo número: \n"))
operation = input("Informe a opeção(+, -, *, /) da calculadora: \n")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num1 == 0 or num2 == 0:
        print("Erro: Não é possível dividir por Zero!")
        result = 0
    else:
        result = num1 / num2
else:
    print("Erro: Operação Inválida!")
    result = 0

print(f"O resultado da conta: {num1:.2f} {operation} {num2:.2f} é: {result:.2f}")