"""Escreva um programa, em Python, para ler do usuário o código (número inteiro), a
descrição e o preço de 20 (vinte) produtos. Cada produto deve ser armazenado como
uma tupla (código, descrição, preço).
Ao final, exibir:
• Descrição do(s) produto(s) mais caro(s);
• Códigos dos produtos com valor abaixo da média."""

produtos = []

for i in range(20):
    codigo = int(input(f'Digite o código do produto {i + 1}: '))
    descricao = input(f'Digite a descricao do produto {i + 1}: ')
    preco = float(input(f'Digite o preço do produto {i + 1}: '))

    produtos.append((codigo, descricao, preco))

# Encontrar o produto mais caro

preco_maximo = max(produto[2] for produto in produtos)

for produto in produtos:
    if produto[2] == preco_maximo:
        descricao = produto[1]
        print(f'Produto mais caro: {descricao}')

media = sum(produto[2] for produto in produtos) / len(produtos)

for produto in produtos:
    if produto[2] < media:
        codigo = produto[0]
        print(f'Código do produto abaixo da média: {codigo}')