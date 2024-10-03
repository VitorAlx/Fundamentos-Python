name = "Vitor Alex"

#string[inicio:fim] - indice começa na posição 0 / indice final -1

#buscar toda a string a partir do indice inicial
print(name[0:])

#buscar toda a string até o indice final
print(name[:10]) #acrescentar +1 por conta do indice final -1, obs: espaço não conta como caractere

"""
string[inicio:fim:passo]
passo é o incremento da verificação, padrão = +1
"""

#buscar a string de 2 em 2 caracteres:
print(name[::2]) #obs: considera espaço como caractere

#inverter uma string de trás para frente:
print(name[::-1])