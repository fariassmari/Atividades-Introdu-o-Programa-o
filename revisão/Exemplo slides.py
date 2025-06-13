""""
Ler uma matriz A, de ordem 2x3 contendo inteiros, gerar uma matriz B onde cada elemento
de B corresponderá ao dobro do respectivo elemento de A.
"""

def criar_matriz(linhas: int, colunas: int) -> list:
    matriz = []
    for i in range(linhas):
        matriz.append([0] * colunas)
    return matriz

matriz_a = criar_matriz(3, 4)
matriz_b = criar_matriz(3, 4)

# Lê os elementos da matriz A e gera a matriz B
for i in range(3):
    for j in range(4):
        matriz_a[i][j] = int(input(f"Elemento A({i},{j}): "))

# Gera a matriz B com o dobro dos elementos de A
for i in range(3):
    for j in range(4):
        matriz_b[i][j] = matriz_a[i][j] * 2

print(f'Matriz A: {matriz_a}')
print(f'Matriz B: {matriz_b}')
