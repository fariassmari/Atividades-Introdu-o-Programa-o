divisor = int(input())
dividendo = int(input())

def resto_divisao(divisor: int, dividendo: int) -> int:
    return divisor % dividendo

resto = resto_divisao(divisor, dividendo)
print(resto)
