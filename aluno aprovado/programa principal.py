import funcoes

# PROGRAMA PRINCIPAL
nome_aluno = input("Nome do aluno: ")

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

media_final = funcoes.media_aritmetica(nota1, nota2, nota3)
situacao_final = funcoes.situacao_aluno(media_final)

print(f'Aluno: {nome_aluno}')
print(f'Média: {media_final:.2f}')
print(f'Situação: {situacao_final}')
