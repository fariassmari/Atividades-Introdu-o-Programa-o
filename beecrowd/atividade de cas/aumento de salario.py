salario = float(input())

def reajuste(salario: float) -> float:
    if salario <= 400.00:
        reajuste_ganho = salario * 0.15
        salario_novo = salario + reajuste_ganho
        percentual = 15
    elif salario >= 400.01 and salario <= 800.00:
        reajuste_ganho = salario * 0.12
        salario_novo = salario + reajuste_ganho
        percentual = 12
    elif salario >= 800.01 and salario <= 1200.00:
        reajuste_ganho = salario * 0.10
        salario_novo = salario + reajuste_ganho
        percentual = 10
    elif salario >= 1200.01 and salario <= 2000.00:
        reajuste_ganho = salario * 0.07
        salario_novo = salario + reajuste_ganho
        percentual = 7
    else:
        reajuste_ganho = salario * 0.04
        salario_novo = salario + reajuste_ganho
        percentual = 4

    return reajuste_ganho, salario_novo, percentual

reajuste_ganho, salario_novo, percentual = reajuste(salario)

print(f'Novo salario: {salario_novo:.2f}')
print(f'Reajuste ganho: {reajuste_ganho:.2f}')
print(f'Em percentual: {percentual} %')

        
