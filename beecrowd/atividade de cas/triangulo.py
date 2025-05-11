valor1, valor2, valor3 = input().split()
valor1, valor2, valor3 = float(valor1), float(valor2), float(valor3)

def forma_triangulo(valor1: float, valor2: float, valor3: float) -> float:
    soma1 = valor1 + valor2
    soma2 = valor1 + valor3
    soma3 = valor2 + valor3
    if soma1 > valor3 and soma2 > valor2 and soma3 > valor1:
        perimetro = valor1 + valor2 + valor3
        return f'Perimetro = {perimetro:.1f}'
    else:
        area = (valor1 + valor2) * valor3 /  2
        return f'Area = {area:.1f}'

resultado = forma_triangulo(valor1, valor2, valor3)

print(resultado)
