"""
Escreva um programa, em Python, para ler 10 (dez) números inteiros. Ao final, exiba o
dobro dos números pares e o triplo dos números ímpares.
"""

lista = []
lista_dobro = []
lista_triplo = []

for i in range(10):
    num = int(input('Digite um número: '))
    lista.append(num)

    if num % 2 == 0:
        dobro = num * 2
        lista_dobro.append(dobro)
    else:
        triplo = num * 3
        lista_triplo.append(triplo) 

print("Lista de números:", lista)
print("Dobro dos números pares:", lista_dobro)
print("Triplo dos números ímpares:", lista_triplo)