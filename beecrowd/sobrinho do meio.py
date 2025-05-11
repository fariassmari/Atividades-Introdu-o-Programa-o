huguinho, zezinho, luisinho = input().split()
huguinho, zezinho, luisinho = int(huguinho), int(zezinho), int(luisinho)

def sobrinho_meio(huguinho: int, zezinho: int, luisinho: int) -> str:
    if huguinho > zezinho and zezinho > luisinho or huguinho < zezinho and zezinho < luisinho:
        return 'zezinho'
    elif zezinho < huguinho and huguinho < luisinho or zezinho > huguinho and huguinho > luisinho:
        return 'huguinho'
    else:
        return 'luisinho'

sobrinho_do_meio = sobrinho_meio(huguinho, zezinho, luisinho)
print(sobrinho_do_meio)
