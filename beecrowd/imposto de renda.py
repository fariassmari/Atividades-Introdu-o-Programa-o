salario = float(input())

def imposto_renda(salario: float) -> str:
    if salario <= 2000.00:
        return 'Isento'
    imposto = 0.0
    if salario > 2000.00:
        if salario >= 2000.01 and salario <= 3000:
            imposto += (salario - 2000) * 0.08
        elif salario >= 3000.01 and salario <= 4500.00:
            imposto += 1000.00 * 0.08
            imposto += (salario - 3000.00) * 0.18
        elif salario > 4500:
            imposto += 1000.00 * 0.08
            imposto += 1500.00 * 0.18
            imposto += (salario - 4500.00) * 0.28
    return f'R$ {imposto:.2f}'
    
imposto = imposto_renda(salario)

print(imposto)
