valor1, valor2, valor3 = input().split()
valor1, valor2, valor3 = float(valor1), float(valor2), float(valor3)

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
            
    return maior, meio, menor

def forma_triangulo(valor1: float, valor2: float, valor3: float) -> str:
    soma = valor2 + valor3
    if valor1 >= soma:
        return 'NAO FORMA TRIANGULO'
    
    if valor1 ** 2 == (valor2 ** 2) + (valor3 ** 2):
         return 'TRIANGULO RETANGULO'
    elif valor1 ** 2 > (valor2 ** 2) + (valor3 ** 2):
        return 'TRIANGULO OBTUSANGULO'
    elif valor1 ** 2 < (valor2 ** 2) + (valor3 ** 2):
        return 'TRIANGULO ACUTANGULO'
        
def lados_triangulo(valor1: float, valor2: float, valor3: float) -> str:
    if valor1 == valor2 and valor2 == valor3:
        return 'TRIANGULO EQUILATERO'
    elif valor1 == valor2 or valor1 == valor3 or valor2 == valor3:
        return 'TRIANGULO ISOSCELES'


maior, meio, menor = ordem(valor1, valor2, valor3)

forma = forma_triangulo(maior, meio, menor)

lados = lados_triangulo(maior, meio, menor)

print(forma)

if lados is not None:
    print(lados)
