"""
Escreva um programa para ler vários nomes, até que o usuário digite “fim”. Ao final,
exiba todos os nomes informados.
"""
nomes = []

while True:
    nome = input("Digite um nome (ou digite 'fim' para encerrar): ")
    if nome.lower() == 'fim':
        break
    nomes.append(nome)

print("Nomes informados:")
for nome in nomes:
    print(nome)