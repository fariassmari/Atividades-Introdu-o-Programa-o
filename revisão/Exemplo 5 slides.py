"""
Gerar uma matriz (3 x 5) com valores inteiros aleatórios (entre 1 e 10), calcular a soma de
cada linha e a soma de cada coluna.
"""
import random

def criar_matriz(linhas: int, colunas: int) -> list:
    matriz = []
    for i in range(linhas):
        matriz.append([0] * colunas)
    return matriz

matriz = criar_matriz(3, 5)

# Gera valores aleatórios entre 1 e 10 para a matriz
for i in range(3):
    for j in range(5):
        matriz[i][j] = random.randint(1,10)

print(f'Matriz: {matriz}')
for i in range(3):
    for j in range(5):
        print(f'{matriz[i][j]:4}', end='')
    print()

# Calcula a soma de cada linha
print('Soma de cada linha:')
for i in range(3):
    soma = 0
    for j in range(5):
        soma += matriz[i][j]
    print(f'{soma:4}')

# Calcula a soma de cada coluna
print('Soma de cada coluna:')
for j in range(5):
    soma = 0
    for i in range(3):
        soma += matriz[i][j]
    print(f'{soma:4}', end='')