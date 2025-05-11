numeros = input().split()

num1 = float(numeros[0])
num2 = float(numeros[1])
num3 = float(numeros[2])

if num1 + num2 > num3 and num1 + num3 > num2 and num2 + num3 > num1:
    perimetro = num1 + num2 + num3
    print(f'Perimetro = {perimetro:.1f}')
else:
    area = ((num1 + num2) * num3) / 2
    print(f'Area = {area:.1f}')
