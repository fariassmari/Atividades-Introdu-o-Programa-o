import math

def area_quadrado(lado: float) -> float:
    """
    Calcula a área da travessa com formato quadrado, elevando o valor do lado ao quadrado.
    
    Parâmetros:
        lado (float): Medida do lado do quadrado.

    Retorno:
        float: Área do quadrado (lado elevado ao quadrado).
    """
    return lado**2

def area_circulo(raio: float) -> float:
    """
    Calcula a área da forma com formato de um círculo, pela fórmula π × raio².

    Parâmetros:
        raio (float): Raio do círculo.

    Retorna:
        float: Área do círculo.

    """
    return (math.pi * (raio ** 2))

def quantidade_formas(lado_travessa: float, diagonal_forma: float) -> int:
    """
    Calcula a quantidade de formas para a travessa.

    Parâmetros:
        lado_travessa(float): Lado da travessa.
        diagonal_forma(float): Diagonal da forma
        
    Retorna:
        inteiro: Quantidade de formas na travessa.
    """
    quantidade_por_linhas = int(lado_travessa // diagonal_forma)
    return quantidade_por_linhas**2

def area_util(qtd_formas: int, area_forma: float)-> float:
    """
    Calcula a área útil ocupada pelas formas.

    Parâmetros:
        qtd_formas(int): Quantidade de formas.
        area_forma(float): Diagonal da forma
        
    Retorna:
        float: Área útil.
    """
    return qtd_formas * area_forma

def area_inutil(area_total: float, area_ocupada: float) -> float:
    """
    Calcula a área inútil que sobrou na travessa.

    Parâmetros:
        area_total(float): Área total da travessa.
        area_ocupada(float): Área ocupada pelas formas.
        
    Retorna:
        float: Área inútil.
    """
    return area_total - area_ocupada

# Testes das funções com valores exemplo
lado_travessa = 58.0  
diagonal_forma = 6.0  # diâmetro da forma redonda em cm

# Cálculos
area_total = area_quadrado(lado_travessa)
raio_forma = diagonal_forma / 2
area_uma_forma = area_circulo(raio_forma)
qtd_formas = quantidade_formas(lado_travessa, diagonal_forma)
area_ocupada = area_util(qtd_formas, area_uma_forma)
area_sobrando = area_inutil(area_total, area_ocupada)

# Impressão dos resultados
print(f'Área da travessa: {area_total:.2f} cm²')
print(f'Raio da forma: {raio_forma:.2f} cm')
print(f'Área da forma redonda: {area_uma_forma:.2f} cm²')
print(f'Quantidade de formas a serem compradas: {qtd_formas}')
print(f'Área útil da travessa (ocupada com pastéis): {area_ocupada:.2f} cm²')
print(f'Área inútil da travessa (massa que sobrou): {area_sobrando:.2f} cm²')
