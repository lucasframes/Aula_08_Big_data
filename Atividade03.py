numeros = []

for i in range(12):
    numero = int(input('digite um numero Inteiro: '))
    numeros.append(numero)

ordenada = sorted(numeros)

print(f'numero em ordem decrecente: {ordenada}')