numeros = []

for i in range(8):
    num = int(input("Digite um número: "))
    numeros.append(num)

lista_ordenada = sorted(numeros)

if numeros == lista_ordenada:
    print("A lista está ordenada.")
else:
    print("A lista não está ordenada.")