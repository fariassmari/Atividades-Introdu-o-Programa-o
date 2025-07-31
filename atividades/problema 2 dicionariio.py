"""O Nordeste possui 9 Estados, sendo eles: AL, BA, CE, MA, PB, PE, PI, RN e SE. Um grupo
é formado por 20 pessoas. Escreva um programa, em Python, para ler de cada pessoa
para qual Estado do nordeste ela gostaria de viajar.
Ao final, exibir:
• Quantidade de votos que cada Estado recebeu;
• Quantidade de votos nulos (foi informado um Estado inválido)."""

estados = ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"]

contagem = {estado: 0 for estado in estados}

votos_nulos = 0

for i in range(20):
    estado = input(f"Pessoa {i + 1}, para qual Estado do Nordeste você gostaria de viajar? ").strip().upper()
    
    if estado in estados:
        contagem[estado] += 1
    else:
        votos_nulos += 1

print("\nQuantidade de votos por Estado:")
for estado, quantidade in contagem.items():
    print(f"{estado}: {quantidade}")

print(f"Votos nulos: {votos_nulos}")
