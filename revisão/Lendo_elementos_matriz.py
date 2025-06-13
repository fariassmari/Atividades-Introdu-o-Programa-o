def matriz(linha: int, coluna: int) -> list:
    matriz = []
    for i in range(linha):
        matriz.append([0]*coluna)
    return matriz

matriz_exemplo = matriz(3, 4)

for i in range(len(matriz_exemplo)):
    for j in range(len(matriz_exemplo[i])):
        matriz_exemplo[i][j] = int(input(f"Elemento {i}, {j}: "))

print(matriz_exemplo)