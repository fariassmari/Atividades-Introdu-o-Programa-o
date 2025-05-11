palavra1 = input()
palavra2 = input()
palavra3 = input()

def tipo_animal(palavra1: str, palavra2: str, palavra3: str) -> str:
    if palavra1 == 'vertebrado':
        if palavra2 == 'ave':
            if palavra3 == 'carnivoro':
                animal = 'aguia'
                return animal
            elif palavra3 == 'onivoro':
                animal = 'pomba'
                return animal
        elif palavra2 == 'mamifero':
            if palavra3 == 'onivoro':
                animal = 'homem'
                return animal
            elif palavra3 == 'herbivoro':
                animal = 'vaca'
                return animal

    elif palavra1 == 'invertebrado':
        if palavra2 == 'inseto':
            if palavra3 == 'hematofago':
                animal = 'pulga'
                return animal
            elif palavra3 == 'herbivoro':
                animal = 'lagarta'
                return animal
        elif palavra2 == 'anelideo':
            if palavra3 == 'hematofago':
                animal = 'sanguessuga'
                return animal
            elif palavra3 == 'onivoro':
                animal = 'minhoca'
                return animal 

    

resultado = tipo_animal(palavra1, palavra2, palavra3)

print(resultado)
