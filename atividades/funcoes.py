def area_triangulo(base: float, altura: float) -> float:
    return (base * altura) / 2

def area_circulo(raio: float) -> float:
    return 3.14159 * (raio ** 2)

def area_trapezio(base_maior: float, base_menor: float, altura: float) -> float:
    return ((base_maior + base_menor) * altura) / 2

def area_quadrado(lado: float) -> float:
    return lado ** 2

def area_retangulo(base: float, altura: float) -> float:
    return base * altura

linha = input().split()
a = float(linha[0])
b = float(linha[1])
c = float(linha[2])

triangulo = area_triangulo(a, c)
circulo = area_circulo(c)
trapezio = area_trapezio(a, b, c)
quadrado = area_quadrado(b)
retangulo = area_retangulo(a, b)

print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')
