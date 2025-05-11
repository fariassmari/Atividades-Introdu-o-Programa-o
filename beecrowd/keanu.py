num = int(input())

def total_casas(num:int) -> int:
    return num ** 2

def casas_brancas(num: int, resultado_total_casas: int) -> int:
    if num % 2 == 0:
        return (resultado_total_casas / 2)
    else:
        return ((resultado_total_casas + 1) // 2)


def casas_pretas(num: int, resultado_total_casas: int) -> int:
    if num % 2 == 0:
        return (resultado_total_casas / 2)
    else:
        return ((resultado_total_casas - 1) // 2)

resultado_total_casas = total_casas(num)
resultado_casas_brancas = casas_brancas(num, resultado_total_casas)
resultado_casas_pretas = casas_pretas(num, resultado_total_casas)

print(f'{resultado_casas_brancas} casas brancas e {resultado_casas_pretas} casas pretas')
