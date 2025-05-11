codigo = int(input())

def codigo_cidades(codigo: int) -> str:
    if codigo == 61:
        destino = 'Brasilia'
    elif codigo == 71:
        destino = 'Salvador'
    elif codigo == 11:
        destino = 'Sao Paulo'
    elif codigo == 21:
        destino = 'Rio de Janeiro'
    elif codigo == 32:
        destino = 'Juiz de Fora'
    elif codigo == 19:
        destino = 'Campinas'
    elif codigo == 27:
        destino = 'Vitoria'
    elif codigo == 31:
        destino = 'Belo Horizonte'
    else:
        destino = 'DDD nao cadastrado'

    return destino

resultado = codigo_cidades(codigo)

print(resultado)
