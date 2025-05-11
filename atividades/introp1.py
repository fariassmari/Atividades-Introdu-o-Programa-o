""" 1-
nome = input('Digite seu nome: ')

idade = input('Digite sua idade: ')
idade = int(idade)

salario = float(input('Salário: '))

dobro_idade = idade * 2"""


""" 2-
nome, idade = input('Digite seu nome e sua idade: ').split()
idade = int(idade)

dia, mes, ano = input('Digite a data (dd/mm/aaaa): ').split('/')
dia, mes, ano = int(dia), int(mes), int(ano)"""



"""3-
nota1, nota2, nota3 = input('Digite as 3 notas: ').split()
nota1, nota2, nota3 = int(nota1), int(nota2), int(nota3)

media = (nota1 + nota2 + nota3) / 3

print(nota1, nota2, nota3)
print(nota1, nota2, nota3, sep='/')
print('media = ', media)
print('media = {media}')
print(f'media = {media:.2f}')"""


valor = 12.23456
print(valor)
print(f'{valor:.2f}')
print(f'{valor:.3f}')
print(f'{valor:.4f}')


