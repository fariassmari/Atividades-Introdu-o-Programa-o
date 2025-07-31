"""Escreva um programa, em Python, para ler as coordenadas (x, y) de vários pontos no
plano cartesiano, armazenando cada ponto como uma tupla. O programa deverá
encerrar quando for informado um ponto na origem (0, 0).
Escreva funções para:
• Exibir todos os pontos digitados;
• Calcular a distância de um determinado ponto até a origem (0, 0);
• Retornar a distância do ponto mais distante da origem;
• Exibir os pontos que estão em um dos eixos (x = 0 ou y = 0).
Ao final, usando as funções criadas, exiba:
• Listar todos os pontos digitados;
• Exibir o valor da distância do ponto que está mais longe da origem;
• Exibir os pontos que estão posicionados em um dos eixos."""

import math 

def exibir_pontos(lista):
    for ponto in lista:
        print(f'Ponto: {ponto}')

def distancia(ponto):
    x, y = ponto
    return math.sqrt(x**2 + y**2)

def ponto_mais_distante(lista):
    distancias = [distancia(ponto) for ponto in lista]
    return max(distancias)

def pontos_em_eixos(lista):
    for ponto in lista:
        if ponto[0] == 0 or ponto[1] == 0:
            print(f'Ponto no eixo: {ponto}')

pontos = []

while True:
    x = float(input('Digite a coordenada x (0 para sair): '))
    y = float(input('Digite a coordenada y (0 para sair): '))

    if x == 0 and y == 0:
        break

    pontos.append((x, y))

print("Pontos digitados:")
exibir_pontos(pontos)

distancia_maxima = ponto_mais_distante(pontos)
print(f'Distância do ponto mais distante da origem: {distancia_maxima:.2f}')

print("Pontos em um dos eixos:")
pontos_em_eixos(pontos)