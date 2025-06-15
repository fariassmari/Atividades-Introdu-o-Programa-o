vetor_a = []

for i in range(100):
    num = float(input())
    vetor_a.append(num)

for i in range(100):
    if vetor_a[i] <= 10:
        print(f'A[{i}] = {vetor_a[i]:.1f}')