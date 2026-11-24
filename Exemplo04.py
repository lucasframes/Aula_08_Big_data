# sets "conjutos"
# coleção mutavel
# nao garante ordem
# nao ha indice

# criar sets vazios
dias = set()
dias.add('segunda')
dias.add('terça')
print(dias)

# conjuntos inicializados
frutas = {'maça', 'uva', 'pera', 'laranja'}
print(frutas)
print(type(frutas))

# remove
frutas.remove('uva')
print(frutas)
print(len(frutas))

# coverter lista para sets
# conjunto_set = set(lista)
# print(conjunto_set)

numeros = [5, 7, 4, 1, 8, 13, 6, 5, 13, 8, 29]
conjunto = set(numeros)
numeros = list(conjunto)
print(len(conjunto))
print(conjunto)