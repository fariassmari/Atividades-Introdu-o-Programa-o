"""
Escreva um programa, em Python, para ler 10 (dez) números inteiros e armazenar em um
vetor. Em seguida, leia um número inteiro e diga se este número está presente no vetor.
"""

lista = []

for i in range(10):
    num = int(input("Digite um número: "))
    lista.append(num)

num_verificar = int(input("Digite um número para verificar se está na lista: "))
if num_verificar in lista:
    print(f"{num_verificar} está na lista.")
else:
    print(f"{num_verificar} não está na lista.")