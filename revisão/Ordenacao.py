lista = []

for i in range(10):
    num = float(input())

    lista.append(num)

ordem = sorted(lista)
print("Lista ordenada:", ordem)
print("Lista original:", lista)