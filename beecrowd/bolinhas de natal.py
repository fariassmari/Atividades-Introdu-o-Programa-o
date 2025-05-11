bolinhas = int(input())
galhos = int(input())

def calcular_bolinhas(galhos: int, bolinhas: int) -> str:
    total_bolinhas = galhos // 2
     if bolinhas >= bolinhas_necessarias:
        return "Amelia tem todas bolinhas!"
    else:
        faltam = bolinhas_necessarias - bolinhas
        return f"Faltam {faltam} bolinha(s)"

bolinhas_faltam = calcular_bolinhas(galhos, bolinhas)

print(bolinhas_faltam)
