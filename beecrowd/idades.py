idades = []

while True:
    idade = int(input())

    if idade < 0:
        break

    idades.append(idade)

    soma = sum(idades)
    media = soma / len(idades)
print(f'{media:.2f}')