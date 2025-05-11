valores = input().split()

valor1 = int(valores[0])
valor2 = int(valores[1])
valor3 = int(valores[2])
valor4 = int(valores[3])

if valor2 > valor3 and valor4 > valor1 and (valor3 + valor4) > (valor1 + valor2) and valor3 > 0 and valor4 > 0 and valor1 % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
    
