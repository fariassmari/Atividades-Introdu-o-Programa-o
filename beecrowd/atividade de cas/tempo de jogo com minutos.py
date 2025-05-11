hora_inicial, minuto_inicial, hora_final, minuto_final = input().split()
hora_inicial, minuto_inicial, hora_final, minuto_final = int(hora_inicial), int(minuto_inicial), int(hora_final), int(minuto_final)

def tempo(hora_inicial: int, minuto_inicial: int, hora_final: int, minuto_final: int):
    tempo_inicial = hora_inicial * 60 + minuto_inicial
    tempo_final = hora_final * 60 + minuto_final

    if tempo_inicial < tempo_final:
        duracao = tempo_final - tempo_inicial
    elif tempo_inicial > tempo_final:
        duracao = (24 * 60 - tempo_inicial) + tempo_final
    else:
        duracao = 24 * 60

    duracao_horas = duracao // 60
    duracao_minutos = duracao % 60

    return duracao_horas, duracao_minutos


duracao_horas, duracao_minutos = tempo(hora_inicial, minuto_inicial, hora_final, minuto_final)

print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")
