leds_por_digito = {
    '0': 6,
    '1': 2,
    '2': 5,
    '3': 5,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 3,
    '8': 7,
    '9': 6
}

N = int(input())

for i in range(N):
    valor = input().strip()

    total_leds = 0
    for digito in valor:
        quantidade_leds = leds_por_digito[digito]
        total_leds += quantidade_leds

    print(f"{total_leds} leds")