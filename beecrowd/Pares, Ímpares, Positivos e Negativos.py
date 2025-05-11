valor1 = int(input())
valor2 = int(input())
valor3 = int(input())
valor4 = int(input())
valor5 = int(input())

def valores_pares(valor1: int, valor2: int, valor3: int, valor4: int, valor5: int) -> str:
    pares = 0
    if valor1 % 2 == 0:
        pares += 1
    if valor2 % 2 == 0:
        pares += 1
    if valor3 % 2 == 0:
        pares += 1
    if valor4 % 2 == 0:
        pares += 1
    if valor5 % 2 == 0:
        pares += 1

    return f'{pares} valor(es) par(es)'

def valores_impares(valor1: int, valor2: int, valor3: int, valor4: int, valor5: int) -> str:
    impares = 0
    if valor1 % 2 != 0:
        impares += 1
    if valor2 % 2 != 0:
        impares += 1
    if valor3 % 2 != 0:
        impares += 1
    if valor4 % 2 != 0:
        impares += 1
    if valor5 % 2 != 0:
        impares += 1

    return f'{impares} valor(es) impar(es)'

def valores_positivos(valor1: int, valor2: int, valor3: int, valor4: int, valor5: int) -> str:
    positivos = 0
    if valor1 > 0:
        positivos += 1
    if valor2 > 0:
        positivos += 1
    if valor3 > 0:
        positivos += 1
    if valor4 > 0:
        positivos += 1
    if valor5 > 0:
        positivos += 1

    return f'{positivos} valor(es) positivo(s)'

def valores_negativos(valor1: int, valor2: int, valor3: int, valor4: int, valor5: int) -> str:
    negativos = 0
    if valor1 < 0:
        negativos += 1
    if valor2 < 0:
        negativos += 1
    if valor3 < 0:
        negativos += 1
    if valor4 < 0:
        negativos += 1
    if valor5 < 0:
        negativos += 1

    return f'{negativos} valor(es) negativo(s)'


pares = valores_pares(valor1, valor2, valor3, valor4, valor5)
impares = valores_impares(valor1, valor2, valor3, valor4, valor5)
positivos = valores_positivos(valor1, valor2, valor3, valor4, valor5)
negativos = valores_negativos(valor1, valor2, valor3, valor4, valor5)

print(pares)
print(impares)
print(positivos)
print(negativos)
