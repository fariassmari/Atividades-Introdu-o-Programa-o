import funcoes

# PROGRAMA PRINCIPAL

nota1 = int(input('Nota 1: ')) 
nota2 = int(input('Nota 2: ')) 
nota3 = int(input('Nota 3: '))

resultado_media_aritmetica = funcoes.media_aritmetica(nota1, nota2, nota3)
resultado_media_ponderada = funcoes.media_ponderada(nota1, nota2, nota3, 2, 3, 5)

print(f'Notas: {nota1, nota2, nota3}') 
print(f'Média aritmética: {resultado_media_aritmetica}')
print(f'Média ponderada: {resultado_media_ponderada}') 

      
