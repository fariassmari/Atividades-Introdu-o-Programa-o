def consumo(distancia: int, combustivel: float) -> float:
    return distancia / combustivel

distancia = int(input())
combustivel = float(input())

consumo_medio = consumo(distancia, combustivel)

print(f'{consumo_medio:.3f} km/l')
