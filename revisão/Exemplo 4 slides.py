"""
Dada uma matriz de inteiros, determinar o maior valor da matriz. Obs: a ordem da matriz
será lida e os elementos serão gerados com valores aleatórios entre 1 e 20.
"""
import random

def criar_matriz(linhas: int, colunas: int) -> list:
    matriz = []
    for i in range(linhas):
        matriz.append([0] * colunas)
    return matriz

linhas, colunas = map(int, input("Digite a ordem da matriz (linhas colunas): ").split())
matriz = criar_matriz(linhas, colunas)

# Gera valores aleatórios entre 1 e 20 para a matriz
for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = random.randint(1,20)
print(f'Matriz: {matriz}')

# Determina o maior valor da matriz
maior = matriz[0][0]
for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
print(f'Maior valor da matriz: {maior}')