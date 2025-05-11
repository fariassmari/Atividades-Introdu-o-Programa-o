num1 = int(input())
num2 = int(input())

if num1 > num2:
    num1, num2 = num2, num1

soma = 0
for i in range(num1 + 1, num2):
    if i % 2 != 0:
        soma += i

print(soma)
