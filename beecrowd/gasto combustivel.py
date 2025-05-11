def distancia(tempo: int, velocidade: int) -> float:
    distancia_percorrida = tempo * velocidade
    return distancia_percorrida / 12

tempo = int(input())
velocidade = int(input())

litros = distancia(tempo, velocidade)

print(f'{litros:.3f}')
