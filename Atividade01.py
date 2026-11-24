vendas = []

for i in range(10):
    valor = float(input('informe o valor das vendas: R$ '))
    vendas.append(valor)

print(vendas)

total = sum(vendas)

print(f'total: R$ {total}')