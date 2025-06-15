"""
Escreva um programa, em Python, para ler 8 (oito) números e armazenar em um vetor
(A). Leia mais 8 (oito) números e armazene em outro vetor (B). Gere um vetor (C), onde
cada elemento é a soma dos correspondentes nos vetores A e B.
"""
vetor_a = []
vetor_b = []
vetor_c = []

for i in range(8):
    num_a = int(input(f'Digite o {i+1}º número para o vetor A: '))
    vetor_a.append(num_a)

for i in range(8):
    num_b = int(input(f'Digite o {i+1}º número para o vetor B: '))
    vetor_b.append(num_b)   

for i in range(8):
    soma = vetor_a[i] + vetor_b[i]
    vetor_c.append(soma)

print("Vetor A:", vetor_a)
print("Vetor B:", vetor_b)
print("Vetor C (soma dos vetores A e B):", vetor_c)