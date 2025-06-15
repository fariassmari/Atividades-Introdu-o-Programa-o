"""
Escreva um programa, em Python, para ler 6 (seis) números. Calcule e exiba o maior
valor e sua respectiva posição.
"""
lista = []
maior = 0

for i in range(6):
    num = int(input('Digite um número: '))
    lista.append(num)

    if num > maior:
        maior = num
    
posicao = lista.index(maior)
print("Lista de números:", lista)
print("Maior valor:", maior)
print("Posição do maior valor:", posicao)