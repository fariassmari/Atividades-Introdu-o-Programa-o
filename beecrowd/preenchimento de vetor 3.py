num = float(input())

vetor = []

for i in range(100):
    vetor.append(num)
    num = num / 2.0

for i in range(100):
    print(f"N[{i}] = {vetor[i]:.4f}")
    
