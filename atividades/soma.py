""" def soma(num1: int, num2: int) -> int:
    return num1 + num2 
    
num1 = int(input())
num2 = int(input())

somar = soma(num1, num2) 

print(f'SOMA = {somar}')"""

"""def area_circulo(raio: float) -> float:
    pi = 3.14159
    return pi * raio ** 2
    
raio = float(input())

area = area_circulo(raio)

print(f'A={area:.4f}')"""

def media_ponderada(nota1: float, nota2: float, nota3: float, peso1: float=2, peso2: float=3, peso3: float=5) -> float:
    return (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)
    
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

media = media_ponderada(nota1, nota2, nota3)

print(f'MEDIA = {media:.1f}')
