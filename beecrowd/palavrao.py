palavra = input()
tamanho = len(palavra)

def palavrao(tamanho: int) -> str:
    if tamanho >= 10:
        return 'palavrao'
    else:
        return 'palavrinha'

resultado = palavrao(tamanho)

print(resultado)
