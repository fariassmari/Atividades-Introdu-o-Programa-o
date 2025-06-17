pessoas = []

for i in range(10):
    nome = input("Digite o nome da pessoa: ").strip()
    idade = int(input("Digite a idade da pessoa: "))
    
    pessoas.append((nome, idade))

soma_idades = 0
for pessoa in pessoas:
    soma_idades += pessoa[1]

media_idades = soma_idades / len(pessoas)

print("Média de idades:", media_idades)
print("Pessoas com idade acima da média:")

for pessoa in pessoas:
    if pessoa[1] > media_idades:
        print(pessoa[0])