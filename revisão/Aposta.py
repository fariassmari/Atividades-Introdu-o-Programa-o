numeros = []

for i in range(6):
    num = float(input())

    if num > 1 and num < 60:
        numeros.append(num)
    else:
        print("Número inválido. Digite um número entre 1 e 60.")

print("Números válidos:", numeros)
