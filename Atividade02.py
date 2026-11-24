numero = []

while True:
    valor = int(input('digite o numero inteiro ou N pra encerrar: '))
    numero.append(valor)
    resposta = input('\nquer continuar [S/N]: ')

    if resposta == 'N':
        break

print(valor)

quantidade = len(numero)

print(f'quantida de numeros: {quantidade}')

                  
                  