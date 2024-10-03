nomeCar = {
    "Modelo":"Corsa",
    "Ano de Lançamento":2001,
    "Cor":"Prata",
    "Leds": ["Luz Baixa", "Placa", "Luz de Ré", "Interior"]
}

print(nomeCar)

#tamanho
print(len(nomeCar))
print(type(nomeCar))

#retornar valor de uma chave
print(nomeCar["Leds"])
print(nomeCar.get("Leds"))


