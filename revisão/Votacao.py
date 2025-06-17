candidatas = []
votos = []
total_votos = []

# Cadastra 2 candidatas
for i in range(2):
    nome = input("Digite o nome da cidade candidata: ").strip()
    candidatas.append(nome)

# Recebe 5 votos
for i in range(5):
    voto = input("Digite o nome da cidade votada: ").strip()
    votos.append(voto)

# Conta os votos de cada candidata
for candidata in candidatas:
    qtd_votos = votos.count(candidata)
    total_votos.append(qtd_votos)
    print(f'{candidata} recebeu {qtd_votos} votos')

# Descobre a vencedora
indice_vencedora = total_votos.index(max(total_votos))
vencedora = candidatas[indice_vencedora]
print(f"\nCidade vencedora: {vencedora}")