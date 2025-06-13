"""
Gerar e imprimir uma matriz quadrada de ordem N (N será lido), onde cada elemento
corresponderá a soma de seus índices. Obs: a matriz deve ser impressa no formato de
matriz.
"""
matriz = []

ordem = int(input("Digite a ordem da matriz: "))

# Cria uma matriz quadrada de ordem N preenchida com zeros
for i in range(ordem):
    matriz.append([0] * ordem)

# Preenche a matriz com a soma dos índices
for i in range(ordem):
    for j in range(ordem):
        matriz[i][j] = i + j

# Imprime a matriz no formato de matriz
for i in range(ordem):
    for j in range(ordem):
        print(f'{matriz[i][j]:4}', end='')
    print() 