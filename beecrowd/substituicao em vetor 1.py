vetor = []

for i in range(10):
    num = int(input())
    vetor.append(num)

    if num <= 0:
        vetor[i] = 1

for i in range(10):
    print(f'X[{i}] = {vetor[i]}') 