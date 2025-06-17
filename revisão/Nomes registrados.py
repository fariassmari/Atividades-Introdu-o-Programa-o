nomes = []

while True:
    nome = input("Digite o nome da pessoa: ").strip()
    
    if nome.lower() == "fim":
        break

    nomes.append(nome)
    
print("Nomes registrados:", nomes)