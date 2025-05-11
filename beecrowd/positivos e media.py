valor1 = float(input())
valor2 = float(input())
valor3 = float(input())
valor4 = float(input())
valor5 = float(input())
valor6 = float(input())

def valores_positivos(valor1: float, valor2: float, valor3: float, valor4: float, valor5: float, valor6: float) -> str:
    positivos = 0
    soma = 0
    if valor1 > 0:
        positivos += 1
        soma += valor1
    if valor2 > 0:
        positivos += 1
        soma += valor2
    if valor3 > 0:
        positivos += 1
        soma += valor3
    if valor4 > 0:
        positivos += 1
        soma += valor4
    if valor5 > 0:
        positivos += 1
        soma += valor5
    if valor6 > 0:
        positivos += 1
        soma += valor6

    media = soma / positivos

    return media, positivos


media, positivos = valores_positivos(valor1, valor2, valor3, valor4, valor5, valor6)

print(f'{positivos} valores positivos')
print(f'{media:.1f}')


