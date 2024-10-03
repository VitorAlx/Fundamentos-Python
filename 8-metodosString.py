name = "Vitor Alex"

descricao = """Esse é um exemplo de uma String Multilinha,
que é declarada com três aspas simples ou duplas, e é
exibida da mesma forma que declarada."""

#transformar tudo em maiúsculo:
print(name.upper())

#transformar tudo em minúsculo:
print(name.lower())

#deixa a primeira letra maiúscula
print(name.capitalize())

#deixa a primeira letra de cada palavra maiúscula (Títulos)
print(name.title())

#retorna a string centralizada com caractere de preenchimento
print(name.center(10, '-'))

#procura um caractere e retorna a posição:
print(name.find("r"))

#altera um elemento por outro
print(name.replace("Alex", "Vermieiro"))

#quebra em mais strings com um elemento de quebra
print(descricao.split(","))