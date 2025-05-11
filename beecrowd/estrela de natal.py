from datetime import datetime, timedelta

# Número de revoluções
revolucoes = int(input())

dias_por_ano = 365.25

# Revoluções a partir da data de 21 de dezembro de 2020
data_inicial = datetime(2020, 12, 21)

def calcular_revolucao(periodo_orbital_anos: float, revolucoes: int) -> int:
    dias = int(periodo_orbital_anos * dias_por_ano * revolucoes)
    data = data_inicial + timedelta(days=dias)
    return dias, data


periodo_jupiter = 11.9
periodo_saturno = 29.6

dias_jupiter, data_jupiter = calcular_revolucao(periodo_jupiter, revolucoes)
dias_saturno, data_saturno = calcular_revolucao(periodo_saturno, revolucoes)

print(f"Dias terrestres para Jupiter = {dias_jupiter}")
print(f"Data terrestre para Jupiter: {data_jupiter.strftime('%Y-%m-%d')}")
print(f"Dias terrestres para Saturno = {dias_saturno}")
print(f"Data terrestre para Saturno: {data_saturno.strftime('%Y-%m-%d')}")
