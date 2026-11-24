produtos = []

for i in range(5):
    produto = input('informe o nome do produto: ')
    produtos.append(produto)

print(produtos)

#acesso ao elemento
n = int(input('digite a posição do elemento acessar: ')) 
print(produtos[n-1]) 


# alterando uma lista "nome de elemento"
produtos[n-1] = input(f'informe o nome do outro elemento na posição {n}: ') 
print(produtos)

# remover da lista
produto_a_remover = input('\nDigite o nome do produto a remover: ')

if produto_a_remover in produtos:
    produtos.remove(produto_a_remover)
print(produtos)
