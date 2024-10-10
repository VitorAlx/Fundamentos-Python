import pprint

carrosDict = {
    "Carro1" : {
        "Modelo":"Corsa",
        "Ano de Lançamento":2001,
        "Cor":"Prata",
        "Leds": ["Luz Baixa", "Placa", "Luz de Ré", "Interior"]
    },
    "Carro2" : {
        "Modelo":"Corolla",
        "Ano de Lançamento":2005,
        "Cor":"Preto",
        "Leds": ["não", "not", "nope"]
    }
}

pp = pprint.PrettyPrinter(depth=4)

pp.pprint(carrosDict)

#buscar valor da chave de um dicionario dentro de outro
print(carrosDict["Carro1"]["Modelo"])

#adicionar mais uma chave em um dicionario dentro de outro
carrosDict["Carro1"]["Rodas"] = "Esportivas"
pp.pprint(carrosDict)

#deletar um dicionario dentro de outro
del carrosDict["Carro2"]
pp.pprint(carrosDict)