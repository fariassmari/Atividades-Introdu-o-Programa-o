def gerar_matriz(linhas:int, colunas:int) -> list:
    matriz = []
    for i in range(linhas):
        matriz.append([0] * colunas)
    return matriz

tela = gerar_matriz(8, 4)


for i in range(20):
    linha, coluna = map(int, input().split())
    tela[linha][coluna] += 1

maior = 0

for linha in tela:
    linha_max = max(linha)
    if linha_max > maior:
        maior = linha_max

for i in range(8):
    for j in range(4):
        if tela[i][j] == maior:
            print(f'{i} {j}')
    