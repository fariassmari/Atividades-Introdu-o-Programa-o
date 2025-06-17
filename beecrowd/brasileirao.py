total_vermelhos = [] 
total_amarelos = []

for i in range(38):
    lista_vermelhos = []
    lista_amarelos = []

    for j in range(20):
        amarelos, vermelhos = map(int, input().split())
        lista_vermelhos.append(vermelhos)
        lista_amarelos.append(amarelos)
    
    total_vermelhos.append(sum(lista_vermelhos))
    total_amarelos.append(sum(lista_amarelos))

for i in range(38):
    print(f'{total_amarelos[i]} {total_vermelhos[i]}')
