hora_inicial, hora_final = input().split()
hora_inicial, hora_final = int(hora_inicial), int(hora_final)

if hora_inicial < hora_final:
    duracao = hora_final - hora_inicial
elif hora_inicial > hora_final:
    duracao = (24 - hora_inicial) + hora_final
else:
    duracao = 24

print(f"O JOGO DUROU {duracao} HORA(S)")
