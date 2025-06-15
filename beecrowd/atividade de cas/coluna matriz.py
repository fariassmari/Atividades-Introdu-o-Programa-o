coluna_indice = int(input())
operacao = input().strip()

matriz = []

for i in range(12):
    linha = []
    for j in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)

valores_coluna = []
for i in range(12):
    valor = matriz[i][coluna_indice]
    valores_coluna.append(valor)


    
