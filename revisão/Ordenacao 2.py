pessoas = []

for i in range(10):
    nome = input("Digite o nome da pessoa: ").strip()
    idade = int(input("Digite a idade da pessoa: "))
    
    pessoas.append((nome, idade))

for i in range(len(pessoas)):
    for j in range(i+1, len(pessoas)):
        if pessoas[i][1] > pessoas[j][1]:
            pessoas[i], pessoas[j] = pessoas[j], pessoas[i]

print("Pessoas ordenadas por idade:")
for pessoa in pessoas:
    print(f"{pessoa[0]} - {pessoa[1]} anos")
