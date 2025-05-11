numero_jogadores = int(input())

def porc_saques(acertos_saques: int, tentativas_saques: int) -> float:
    return (acertos_saques / tentativas_saques) * 100

def porc_bloqueios(acertos_bloqueios: int, tentativas_bloqueios: int) -> float:
    return (acertos_bloqueios / tentativas_bloqueios) * 100

def porc_ataques(acertos_ataques: int, tentativas_ataques: int) -> float:
    return (acertos_ataques / tentativas_ataques) * 100

total_tentativas_saques = 0
total_tentativas_bloqueios = 0
total_tentativas_ataques = 0
total_acertos_saques = 0
total_acertos_bloqueios = 0
total_acertos_ataques = 0

for i in range(numero_jogadores):
    nome = input()
    tentativas = input().split()
    acertos = input().split()
    
    total_tentativas_saques += int(tentativas[0])
    total_tentativas_bloqueios += int(tentativas[1])
    total_tentativas_ataques += int(tentativas[2])
    total_acertos_saques += int(acertos[0])
    total_acertos_bloqueios += int(acertos[1])
    total_acertos_ataques += int(acertos[2])

pontos_saques = porc_saques(total_acertos_saques, total_tentativas_saques)
pontos_bloqueios = porc_bloqueios(total_acertos_bloqueios, total_tentativas_bloqueios)
pontos_ataques = porc_ataques(total_acertos_ataques, total_tentativas_ataques)
    
print(f'Pontos de Saque: {pontos_saques:.2f} %.')
print(f'Pontos de Bloqueio: {pontos_bloqueios:.2f} %.')
print(f'Pontos de Ataque: {pontos_ataques:.2f} %.')
