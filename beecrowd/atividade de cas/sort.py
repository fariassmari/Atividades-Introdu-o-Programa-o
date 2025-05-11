valor1, valor2, valor3 = input().split()
valor1, valor2, valor3 = int(valor1), int(valor2), int(valor3)

def ordem(valor1: int, valor2: int, valor3: int) -> int:
    if valor1 >= valor2 and valor1 >= valor3:
        maior = valor1
        if valor2 > valor3:
            meio, menor = valor2, valor3
        else:
            meio, menor = valor3, valor2
    elif valor2 >= valor1 and valor2 >= valor3:
        maior = valor2
        if valor1 > valor3:
            meio, menor = valor1, valor3
        else:
            meio, menor = valor3, valor1
    else:
        maior = valor3
        if valor1 > valor2:
            meio, menor = valor1, valor2
        else:
            meio, menor = valor2, valor1
            
    return menor, meio, maior


menor, meio, maior = ordem(valor1, valor2, valor3)

print(menor)
print(meio)
print(maior)

print()

print(valor1)
print(valor2)
print(valor3)
