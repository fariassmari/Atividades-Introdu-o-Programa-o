"""Escreva um programa, em Python, para ler do usuário o código (número inteiro), a
descrição e o preço de 20 (vinte) produtos. Cada produto deve ser armazenado como
uma tupla (código, descrição, preço).
Ao final, exibir:
• Descrição do(s) produto(s) mais caro(s);
• Códigos dos produtos com valor abaixo da média."""

produtos = []

for i in range(20):
    codigo = int(input(f'Digite o código do produto {i + 1}: '))
    descricao = int(input(f'Digite a descricao do produto {i + 1}: '))
    preco = float(input(f'Digite o preço do produto {i + 1}: '))

    produtos.append((codigo, descricao, preco))

# Encontrar o produto mais caro
precos = []
for produto in produtos:
    preco = produto[2]
    precos.append(preco)

preco_maximo = max(precos)

for produto in preco_maximo:
    descricao = produto[1]
    print(f'Produto mais caro: {descricao}')

media = sum(produtos) / len(produtos)



