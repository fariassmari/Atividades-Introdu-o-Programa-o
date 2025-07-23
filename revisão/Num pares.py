lista = []

for i in range(6):
    num = int(input('Digite o número {i+1}: '))
    if num % 2 == 0:
        lista.append(num)

print(lista)