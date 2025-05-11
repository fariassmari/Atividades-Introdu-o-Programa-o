quantidade_elfos = int(input())

horas_bonecos = 0
horas_arquitetos = 0
horas_musicos = 0
horas_desenhistas = 0

for _ in range(quantidade_elfos):
    nome, grupo, horas = input().split()
    horas = int(quantidade_horas)
    
    if grupo == 'bonecos':
        horas_bonecos += horas
    elif grupo == 'arquitetos':
        horas_arquitetos += horas
    elif grupo == 'musicos':
        horas_musicos += horas
    elif grupo == 'desenhistas':
        horas_desenhistas += horas

total_presentes = (horas_bonecos // 8) + (horas_arquitetos // 4) + (horas_musicos // 6) + (horas_desenhistas // 12)

print(total_presentes)
