valor_x, valor_y = input().split()
valor_x, valor_y = float(valor_x), float(valor_y)

def coordenadas_ponto(valor_x: float, valor_y: float) -> str:
    if valor_x == 0 and valor_y == 0:
        return 'Origem'
    elif valor_x == 0:
        return 'Eixo Y'
    elif valor_y == 0:
        return 'Eixo X'
    elif valor_x > 0 and valor_y > 0:
        return 'Q1'
    elif valor_x < 0 and valor_y > 0:
        return 'Q2'
    elif valor_x < 0 and valor_y < 0:
        return 'Q3'
    else:
        return 'Q4'

coordenadas =  coordenadas_ponto(valor_x, valor_y)
print(coordenadas)
