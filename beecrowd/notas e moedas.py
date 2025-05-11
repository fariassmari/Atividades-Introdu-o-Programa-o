def converte_centavos(valor: float) -> int:
    return int(round(valor * 100))

def notas_cem(valor: int) -> int:
    return valor // 10000

def notas_cinquenta(valor: int) -> int:
    return (valor % 10000) // 5000

def notas_vinte(valor: int) -> int:
    return (valor % 5000) // 2000

def notas_dez(valor: int) -> int:
    return (valor % 2000) // 1000

def notas_cinco(valor: int) -> int:
    return (valor % 1000) // 500

def notas_dois(valor: int) -> int:
    return (valor % 500) // 200

def moedas_um_real(valor: int) -> int:
    return (valor % 200) // 100

def moedas_cinquenta(valor: int) -> int:
    return (valor % 100) // 50

def moedas_vinte_cinco(valor: int) -> int:
    return (valor % 50) // 25

def moedas_dez(valor: int) -> int:
    return (valor % 25) // 10

def moedas_cinco(valor: int) -> int:
    return (valor % 10) // 5

def moedas_um_centavo(valor: int) -> int:
    return valor % 5

# Entrada do valor
valor_recebido = float(input())

# Converte para centavos para evitar erros com ponto flutuante
centavos = converte_centavos(valor_recebido)

# Calcula quantidade de cada nota e moeda
nota100 = notas_cem(centavos)
nota50 = notas_cinquenta(centavos)
nota20 = notas_vinte(centavos)
nota10 = notas_dez(centavos)
nota5 = notas_cinco(centavos)
nota2 = notas_dois(centavos)
moeda1 = moedas_um_real(centavos)
moeda50 = moedas_cinquenta(centavos)
moeda25 = moedas_vinte_cinco(centavos)
moeda10 = moedas_dez(centavos)
moeda5 = moedas_cinco(centavos)
moeda01 = moedas_um_centavo(centavos)

# Exibe resultado
print("NOTAS:")
print(f"{nota100} nota(s) de R$ 100.00")
print(f"{nota50} nota(s) de R$ 50.00")
print(f"{nota20} nota(s) de R$ 20.00")
print(f"{nota10} nota(s) de R$ 10.00")
print(f"{nota5} nota(s) de R$ 5.00")
print(f"{nota2} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{moeda1} moeda(s) de R$ 1.00")
print(f"{moeda50} moeda(s) de R$ 0.50")
print(f"{moeda25} moeda(s) de R$ 0.25")
print(f"{moeda10} moeda(s) de R$ 0.10")
print(f"{moeda5} moeda(s) de R$ 0.05")
print(f"{moeda01} moeda(s) de R$ 0.01")
