indice_linha = int(input())
operacao = input().strip()

matriz = []

for i in range(12):
    linha_atual = []
    for j in range(12):
        valor = float(input().strip())
        linha_atual.append(valor)
    matriz.append(linha_atual)

valores_linha = matriz[indice_linha]
soma = sum(valores_linha)

if operacao == 'S':
    print(f"{soma:.1f}")
elif operacao == 'M':
    media = soma / len(valores_linha)
    print(f"{media:.1f}")
