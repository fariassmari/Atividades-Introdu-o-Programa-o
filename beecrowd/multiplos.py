num1, num2 = input().split()
num1, num2 = int(num1), int(num2)

def multiplos(num1: int, num2: int) -> str:
    if num1 % num2 == 0 or num2 % num1 == 0:
        return 'Sao Multiplos'
    else:
        return 'Nao sao Multiplos' 

resultado = multiplos(num1, num2)

print(resultado)
