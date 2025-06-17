vetor = []

valor = int(input())
for i in range(1000):
    for j in range(valor):
        vetor.append(j)
    print(f"N[{i}] = {vetor[i]}")