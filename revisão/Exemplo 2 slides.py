"""
Ler uma matriz A de ordem M x N (obs: M e N serão lidos) contendo inteiros, calcular a
soma de todos os seus elementos.
"""
def criar_matriz(linhas: int, colunas: int) -> list:
    matriz = []
    for i in range(linhas):
        matriz.append([0] * colunas)
    return matriz

# Lê a ordem da matriz
print('Digite a ordem da matriz')
linhas, colunas = map(int, input('Número de linhas e colunas: ').split())
matriz_a = criar_matriz(linhas, colunas)

# Lê os elementos da matriz 
for i in range(linhas):
    for j in range(colunas):
        matriz_a[i][j] = int(input(f"Elemento ({i},{j}): "))
print(f'Matriz A: {matriz_a}')

# Calcula a soma dos elementos da matriz
soma = 0
for i in range(linhas):
    for j in range(colunas):
        soma += matriz_a[i][j]
print(f'Soma dos elementos da matriz A: {soma}')