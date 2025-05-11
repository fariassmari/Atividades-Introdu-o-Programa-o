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

    return pares


pares = valores_pares(valor1, valor2, valor3, valor4, valor5)

print(f'{pares} valores pares')
