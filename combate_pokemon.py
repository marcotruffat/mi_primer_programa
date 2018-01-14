pokemon_elejido = input("¿Contra que pokemon quieres combatir? (Squirtle / Charmander / Bulbasur)")
vida_pikachu = 100
vida_enemigo = 0
ataque_pokemon = 0

if pokemon_elejido == "Squirtle":
    vida_enemigo = 90
    nombre_pokemon = "Squirtle"
    ataque_pokemon = 8

elif pokemon_elejido == "Charmander":
    vida_enemigo = 80
    nombre_pokemon = "Charmander"
    ataque_pokemon = 7

elif pokemon_elejido == "Bulbasur":
    vida_enemigo = 100
    nombre_pokemon = "Bulbasur"
    ataque_elegido = 10

while vida_enemigo > 0 and vida_pikachu > 0:
    ataque_elegido = input("¿Que ataque quieres hacer? (Chispazo / Bola voltio)")
    if ataque_elegido == "Chispazo":
        vida_enemigo -= ataque_pokemon

    elif ataque_elegido == "Bola voltio":
        vida_enemigo -= ataque_pokemon

    print("La vida de {} ahora es de {}".format(nombre_pokemon, vida_enemigo))

    print("{} te hace una ataque de {}".format(nombre_pokemon, ataque_pokemon))
    vida_pikachu -= ataque_pokemon
    print("La vida de pikachu es de {}".format(vida_pikachu))

if vida_enemigo <= 0:
    print("Has ganado!")

elif vida_pikachu <= 0:
    print("Has perdido.")

print("El combate ha terminado.")
