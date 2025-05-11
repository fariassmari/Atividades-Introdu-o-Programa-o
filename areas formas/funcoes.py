import math

def area_quadrado(lado: float)-> float:
    """
    Calcula a área de um quadrado, elevando o valor do lado ao quadrado.
    
    Parâmetros:
        lado (float): Medida do lado do quadrado.

    Retorno:
        float: Área do quadrado (lado elevado ao quadrado).
    """
    return lado**2

def area_retangulo(base: float, altura: float) -> float:
    """
    Calcula a área de um retângulo, multiplicando a base pela altura.
    
    Parâmetros:
        base (float): Comprimento da base do retângulo.
        altura (float): Altura do retângulo.

    Retorna:
        float: Área do retângulo.
    """
    return base * altura

def area_triangulo(base: float, altura: float) -> float:
    """
    Calcula a área de um triângulo, pela fórmula(base × altura) / 2.
    
    Parâmetros:
        base (float): Comprimento da base do triângulo.
        altura (float): Altura do triângulo.

    Retorna:
        float: Área do triângulo.
    """
    return (base * altura) / 2

def area_trapezio(base_maior: float, base_menor: float, altura: float) -> float:
    """
    Calcula a área de um trápezio, pela fórmula ((base maior + base menor) × altura) / 2.
    
    Parâmetros:
        base_maior (float): Comprimento da base maior do trapézio.
        base_menor (float): Comprimento da base menor do trapézio.
        altura (float): Altura do trapézio.

    Retorna:
        float: Área do trapézio.
    """
    return ((base_maior + base_menor) * altura) / 2

def area_paralelogramo(base: float, altura: float) -> float:
    """
    Calcula a área de um paralelogramo, multiplicando a base pela altura.

    Parâmetros:
        base (float): Comprimento da base do paralelogramo.
        altura (float): Altura do paralelogramo.

    Retorna:
        float: Área do paralelogramo.
    """
    return base * altura

def area_losango(diagonal_maior: float, diagonal_menor: float) -> float:
    """
    Calcula a área de um losango, pela fórmula (diagonal maior × diagonal menor) / 2.

    Parâmetros:
        diagonal_maior (float): Comprimento da diagonal maior do losango.
        diagonal_menor (float): Comprimento da diagonal menor do losango.

    Retorna:
        float: Área do losango.
    """
    return (diagonal_maior * diagonal_menor) / 2

def area_circulo(raio: float) -> float:
    """
    Calcula a área de um círculo, pela fórmula π × raio².

    Parâmetros:
        raio (float): Raio do círculo.

    Retorna:
        float: Área do círculo.

    """
    return (math.pi * (raio ** 2))
