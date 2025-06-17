def gerar_matriz(linhas: int, colunas: int) -> list:
    matriz = []
    for i in range(linhas):
        matriz.append([0] * colunas)
    return matriz

def posicao_valida(x: int, y: int) -> bool:
    return 0 <= x < 4 and 0 <= y < 6

campo = gerar_matriz(4, 6)

bombas = int(input())

for i in range(bombas):
    linha, coluna = map(int, input().split())
    campo[linha-1][coluna-1] = 'B' 

x, y = map(int, input().split())
x -= 1
y -= 1

if campo[x][y] == 'B':
    print('B')
else:
    bombas_redor = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            nx =  x + i
            ny = y + j
            if posicao_valida(nx, ny) and campo[nx][ny] == 'B':
                bombas_redor += 1
                
    if bombas_redor > 0:
        print(bombas_redor)
    else:
        print('X')
