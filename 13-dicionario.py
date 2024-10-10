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

#retornar apenas as chaves do dicionario
print(nomeCar.keys())

#retornar apenas os valores do dicionario
print(nomeCar.values())

#retornar chave e valor
print(nomeCar.items())

#adicionar mais uma chave e valor
nomeCar["Rodas"] = "Esportivas"
print(nomeCar)

#atualizar valores no dicionario
nomeCar.update({"Rodas":"Esportivas de Alumínio"})
print(nomeCar)

nomeCar.pop("Rodas")
print(nomeCar)