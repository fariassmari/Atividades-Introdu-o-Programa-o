"""
Escreva um programa, em Python, para ler 6 (seis) números inteiros. Ao final, exiba todos
os números pares que foram informados.
"""

lista = []

for i in range(6):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        lista.append(num)
        print("Lista de números pares:", lista)
    else:
        print(f"{num} não é par, não será adicionado à lista.")

    