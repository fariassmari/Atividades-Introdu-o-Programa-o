import random
import re

def digito_verificador(cpf_parcial):
    # Primeiro dígito verificador
    soma1 = 0
    for i in range(9):
        soma1 += int(cpf_parcial[i]) * (10 - i)
    resto1 = soma1 % 11

    if resto1 < 2:
        d1 = 0
    else:
        d1 = 11 - resto1

    # Segundo dígito verificador
    cpf_com_d1 = cpf_parcial + str(d1)
    soma2 = 0
    for i in range(10):
        soma2 += int(cpf_com_d1[i]) * (11 - i)
    resto2 = soma2 % 11

    if resto2 < 2:
        d2 = 0
    else:
        d2 = 11 - resto2

    return str(d1) + str(d2)

def gerar_cpf() -> str:
    cpf_base = ''
    for _ in range(9):
        cpf_base += str(random.randint(0, 9))
    digitos = digito_verificador(cpf_base)
    cpf_completo = cpf_base + digitos
    return f"{cpf_completo[:3]}.{cpf_completo[3:6]}.{cpf_completo[6:9]}-{cpf_completo[9:]}"

def validar_cpf(cpf: str) -> bool:
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    cpf_base = cpf[:9]
    digitos_verificadores = digito_verificador(cpf_base)

    return cpf.endswith(digitos_verificadores)


# main

entrada = input("Digite um CPF: ")

if validar_cpf(entrada):
    print("CPF válido!")
else:
    print("CPF inválido!")

print("10 CPFs válidos gerados aleatoriamente: ")

for contador in range(1, 11):
    cpf_gerado = gerar_cpf()
    print(f"{contador}. {cpf_gerado}")