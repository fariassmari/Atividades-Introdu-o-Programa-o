nota1 = int(input('Nota 1: ')) # Estava faltando transformar em inteiro - C
nota2 = int(input('Nota 2: ')) # Estava faltando transformar em inteiro - C
nota3 = int(input('Nota 3: ')) # Estava faltando transformar em inteiro - C

media_aritmetica = (nota1 + nota2 + nota3) / 3 # Faltando parênteses - E
media_ponderada = (nota1 * 2 + nota2 * 2 + nota3 * 5) / 10 # Soma dos pesos erradas - E

media_final = media_aritmetica / media_ponderada

print('Notas: ', nota1, nota2, nota3) # Estava faltando a vírgula - C
print('Média aritmética: ', media_aritmetica)
print(f'Média ponderada: {media_ponderada}') # Faltando chaves - C
print(f'Média final = {media_final}') # Faltando f - C
      
