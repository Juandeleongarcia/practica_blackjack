import random
cartas = {chr(0x1f0a1): 11, chr(0x1f0a2): 2, chr(0x1f0a3): 3, chr(0x1f0a4): 4,
    chr(0x1f0a5): 5, chr(0x1f0a6): 6, chr(0x1f0a7): 7, chr(0x1f0a8): 8,
    chr(0x1f0a9): 9, chr(0x1f0aa): 10, chr(0x1f0ab): 10, chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,

    chr(0x1f0b1): 11, chr(0x1f0b2): 2, chr(0x1f0b3): 3, chr(0x1f0b4): 4,
    chr(0x1f0b5): 5, chr(0x1f0b6): 6, chr(0x1f0b7): 7, chr(0x1f0b8): 8,
    chr(0x1f0b9): 9, chr(0x1f0ba): 10, chr(0x1f0bb): 10, chr(0x1f0bd): 10,
    chr(0x1f0be): 10,

    chr(0x1f0c1): 11, chr(0x1f0c2): 2, chr(0x1f0c3): 3, chr(0x1f0c4): 4,
    chr(0x1f0c5): 5, chr(0x1f0c6): 6, chr(0x1f0c7): 7, chr(0x1f0c8): 8,
    chr(0x1f0c9): 9, chr(0x1f0ca): 10, chr(0x1f0cb): 10, chr(0x1f0cd): 10,
    chr(0x1f0ce): 10,

    chr(0x1f0d1): 11, chr(0x1f0d2): 2, chr(0x1f0d3): 3, chr(0x1f0d4): 4,
    chr(0x1f0d5): 5, chr(0x1f0d6): 6, chr(0x1f0d7): 7, chr(0x1f0d8): 8,
    chr(0x1f0d9): 9, chr(0x1f0da): 10, chr(0x1f0db): 10, chr(0x1f0dd): 10,
    chr(0x1f0de): 10,
}

lista_cartas = list(cartas.keys())
def valor_carta(carta):
    return cartas[carta]

carta1_jugador = random.choice(lista_cartas)
carta2_jugador = random.choice(lista_cartas)

puntuacion_jugador = valor_carta(carta1_jugador) + valor_carta(carta2_jugador)

carta1_banca = random.choice(lista_cartas)
carta2_banca = random.choice(lista_cartas)

puntuacion_banca = valor_carta(carta1_banca) + valor_carta(carta2_banca)

print(f"Jugador: Carta 1 = {carta1_jugador}, Carta 2 = {carta2_jugador}, Puntuación = {puntuacion_jugador}")
print(f"Banca: Carta 1 = {carta1_banca}, Carta 2 = {carta2_banca}, Puntuación = {puntuacion_banca}")

limite_ganador = 21

if puntuacion_jugador == limite_ganador:
    print("Blackjack, jugador ha ganado")

elif puntuacion_banca == limite_ganador:
    print("Blackjack, la banca gana")

elif puntuacion_banca > limite_ganador:
    print("la banca se ha pasado, gana el jugador")

elif puntuacion_jugador > limite_ganador:
    print("el jugador se ha pasado, gana la banca")

elif puntuacion_jugador == puntuacion_banca:
    print("Empate, gana el jugador")

elif puntuacion_jugador > puntuacion_banca:
    print("El jugador gana, la banca pierde")

elif puntuacion_banca > puntuacion_jugador:
    print("La banca gana, el jugador pierde")
