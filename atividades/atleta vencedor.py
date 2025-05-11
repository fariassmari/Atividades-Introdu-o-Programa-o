# Primeiro Jogador
hora = int(input('Hora que o jogador 1 terminou: '))
minuto = int(input('Minuto que o jogador 1 terminou: '))
segundo = int(input('Segundo que o jogador 1 terminou: '))
tempo_jogador_1 = hora * 3600 + minuto * 60 + minuto

# Segundo Jogador
hora = int(input('Hora que o jogador 2 terminou: '))
minuto = int(input('Minuto que o jogador 2 terminou: '))
segundo = int(input('Segundo que o jogador 2 terminou: '))
tempo_jogador_2 = hora * 3600 + minuto * 60 + minuto

# Função que calcula o atleta vencedor ou se os dois atletas empataram
def atleta_vencedor(tempo_jogador_1: int, tempo_jogador_2: int) -> str:
    if tempo_jogador_1 < tempo_jogador_2:
        diferenca = tempo_jogador_2 - tempo_jogador_1
        hora = diferenca // 3600
        minuto = diferenca % 3600 // 60
        segundo = diferenca % 3600 % 60
        return f'Jogador 1 ganhou com vantagem de {hora:02}:{minuto:02}:{segundo:02}'
    elif tempo_jogador_2 < tempo_jogador_1:
        diferenca = tempo_jogador_1 - tempo_jogador_2
        hora = diferenca // 3600
        minuto = diferenca % 3600 // 60
        segundo = diferenca % 3600 % 60
        return f'Jogador 2 ganhou com vantagem de {hora:02}:{minuto:02}:{segundo:02}'
    else:
        return f'Empataram'

resultado = atleta_vencedor(tempo_jogador_1, tempo_jogador_2)

# Imprime o resultado 
print(resultado)
