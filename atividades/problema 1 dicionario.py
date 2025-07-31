"""Escreva um programa, em Python, para ler várias palavras até que o usuário digite "fim".
O programa deve usar um dicionário para contar quantas vezes cada palavra foi digitada.
Ao final, exiba cada palavra e sua respectiva contagem."""

contagem = {}

while True:
    palavra = input("Digite uma palavra (ou 'fim' para encerrar):")

    if palavra.lower() == "fim":
        break

    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

for palavra, quantidade in contagem.items():
    print(f"{palavra}: {quantidade}")