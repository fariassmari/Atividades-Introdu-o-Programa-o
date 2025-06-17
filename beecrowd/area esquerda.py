operacao = input().strip()
matriz = []

for i in range(12):
    linha = []
    for j in range(12):
        valor = float(input().strip())
        linha.append(valor)
    matriz.append(linha)

soma = 0
contador = 0

for i in range(1, 11):
    for j in range(0, 5):
        if (i <= 5 and j < i) or (i >= 6 and j < 11 - i):
            soma += matriz[i][j]
            contador += 1

if operacao == 'S':
    print(f'{soma:.1f}')
elif operacao == 'M':
    media = soma / contador
    print(f'{media:.1f}')