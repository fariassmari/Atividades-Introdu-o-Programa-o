def somar(num1:int, num2:int) -> int:
    """Retorna a soma de num1 e num2."""
    return num1 + num2

def dividir(num1:int, num2:int) -> int:
    """Retorna a divisão de num1 por num2."""
    return num1 / num2

def multiplicar(num1:int, num2:int) -> int:
    """Retorna o resultado da multiplicação de num1 e num2."""
    return num1 * num2

def subtrair(num1:int, num2:int) -> int:
    """Retorna a subtração de num1 e num2."""
    return num1 - num2

def exibir(num1:int, num2:int) -> int:
     return num1, num2

def mensagem_pt() -> str:
    """Retorna uma mensagem de boas-vindas em português."""
    return 'Olá, bem-vindo ao programa de operações matemáticas!'

def mensagem_en() -> str:
    """Retorna uma mensagem de boas-vindas em inglês."""
    return 'Hello, welcome to the math operations program!'

def boas_vindas() -> str:
    """Retorna a mensagem de boas-vindas em português."""
    return mensagem_pt()

n1, n2 = 10, 20

valores = exibir(n1, n2)

print(boas_vindas())
print(mensagem_en())
print("Valores exibidos:", valores)
print(f'{somar(n1, n2) = }')
print(f'{subtrair(n1, n2) = }')
print(f'{multiplicar(n1, n2) = }')
print(f'{dividir(n1, n2) = }')
