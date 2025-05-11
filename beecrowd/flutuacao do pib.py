flutuacao1, flutuacao2 = input().split()
flutuacao1, flutuacao2 = float(flutuacao1), float(flutuacao2)

def flutuacao_pib(flutuacao1: float, flutuacao2: float) -> float: 
    return (1 + flutuacao1 / 100) * (1 + flutuacao2 / 100) -1

resultado_pib = flutuacao_pib(flutuacao1, flutuacao2) * 100
print(f'{resultado_pib:.6f}')

