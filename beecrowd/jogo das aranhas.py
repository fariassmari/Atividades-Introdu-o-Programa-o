num = int(input())  # Quantidade N de aranhas venenosas/inofensivas

# Gera uma lista de aranhas com índices de 0 a 2N-1
def criar_circulo(num: int) -> list[int]:
    return list(range(2 * num))

# Diz se a aranha é venenosa (se está nas posições >= N)
def venenosa(posicao: int, num: int) -> bool:
    return posicao >= num

# Simula a eliminação das aranhas com o passo K
def merlin_vence(num: int, k: int) -> bool:
    vivos = criar_circulo(num)
    idx = 0

    for _ in range(num):  # Precisamos matar exatamente N aranhas
        idx = (idx + k - 1) % len(vivos)
        aranha_morta = vivos[idx]
        
        if not venenosa(aranha_morta, num):  # Se matou uma inofensiva
            return False
        
        vivos.pop(idx)  # Remove a aranha da lista

    return True  # Todas eram venenosas

# Busca o menor K possível que faz Merlin vencer
def encontrar_k(num: int) -> int:
    k = 1
    while True:
        if merlin_vence(num, k):
            return k
        k += 1

k = encontrar_k(num)
print(k)
