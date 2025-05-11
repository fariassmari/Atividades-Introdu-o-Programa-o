nota1, nota2, nota3, nota4 = input().split()
nota1, nota2, nota3, nota4 = float(nota1), float(nota2), float(nota3), float(nota4)

def media_ponderada(nota1: float, nota2: float, nota3: float, nota4: float, peso1: int=2, peso2: int=3, peso3: int=4, peso4: int=1) -> float:
    return (nota1 * peso1 + nota2 * peso2 + nota3 * peso3 + nota4 * peso4) / (peso1 + peso2 + peso3 + peso4)

media = media_ponderada(nota1, nota2, nota3, nota4)

if media >= 7.0:
    print(f'Media: {media:.1f}')
    print('Aluno aprovado.')
elif media < 5.0:
    print(f'Media: {media:.1f}')
    print('Aluno reprovado.')
else:
    print(f'Media: {media:.1f}')
    print('Aluno em exame.')
    nota_exame = float(input())
    print(f'Nota do exame: {nota_exame:.1f}')
    nova_media = (media + nota_exame) / 2
    if nova_media >= 5:
        print('Aluno aprovado.')
        print(f'Media final: {nova_media:.1f}')
    else:
        print('Aluno reprovado.')
        print(f'Media final: {nova_media:.1f}')







