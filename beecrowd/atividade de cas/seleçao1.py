valor1, valor2, valor3, valor4 = input().split()
valor1, valor2, valor3, valor4 = int(valor1), int(valor2), int(valor3), int(valor4)

def validacao_valores(valor1: int, valor2: int, valor3: int, valor4: int) -> str:
    soma1 = valor3 + valor4
    soma2 = valor2 + valor1
    if valor2 > valor3 and valor4 > valor1 and soma1 > soma2 and valor3 > 0 and valor4 > 0 and valor1 % 2 == 0:

        return "Valores aceitos"
    else: 
        return "Valores nao aceitos"
        
resultado = validacao_valores(valor1, valor2, valor3, valor4)

print(resultado)
