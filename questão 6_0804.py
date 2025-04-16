# Solicita ao usuário a hora, o minuto e o segundo de chegada do primeiro colocado
hora_primeiro, minuto_primeiro, segundo_primeiro = input('Início: ').split(':')
# Solicita ao usuário a hora, o minuto e o segundo de chegada do segundo colocado
hora_segundo, minuto_segundo, segundo_segundo = input('Fim: ').split(':')


# Transforma os valores obtidos do primeiro colocado em inteiro
hora_primeiro, minuto_primeiro, segundo_primeiro = int(hora_primeiro), int(minuto_primeiro), int(segundo_primeiro)
# Transforma os valores obtidos do segundo colocado em inteiro
hora_segundo, minuto_segundo, segundo_segundo = int(hora_segundo), int(minuto_segundo), int(segundo_segundo)


# Converte o tempo do primeiro colocado em segundos
tempo_primeiro = hora_primeiro * 3600 + minuto_primeiro * 60 + segundo_primeiro
# Converte o tempo do segundo colocado em segundos
tempo_segundo = hora_segundo * 3600 + minuto_segundo * 60 + segundo_segundo


# Calcula a diferença de tempo entre o segundo colocado e o primeiro colocado, em segundos
diferenca_tempo = tempo_segundo - tempo_primeiro

# Calcula a quantidade de horas entre a diferença do segundo colocado e o primeiro colocado
diferenca_hora = diferenca_tempo // 3600
# Calcula a quantidade de minutos entre a diferença do segundo colocado e o primeiro colocado
diferenca_minuto = diferenca_tempo % 3600 // 60
# Calcula a quantidade de segundos entre a diferença do segundo colocado e o primeiro colocado
diferenca_segundo = diferenca_tempo % 3600 % 60

# Imprime a diferença na tela no formato h:m:s
print(f'Diferença: {diferenca_hora}:{diferenca_minuto}:{diferenca_segundo}')
