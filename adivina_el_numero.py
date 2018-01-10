number_to_guess = 2
user_number = int(input("Adivina el numero del 1 al 10: "))

if user_number == number_to_guess:
    print("Has Ganado!!")

else:
    print("has perdido")
    user_number = int(input("Adivina el numero... "))

    if user_number == number_to_guess:
        print("Muy bien")

    else:
        print("has perdido")
        user_number = int(input("Prueba otra vez: "))

        if user_number == number_to_guess:
            print("Has ganado")

        else:
            print("has perdido")
            user_number = int(input("Aun no lo sabes? Prueba otra vez: : "))

            if user_number == number_to_guess:
                print("Por fin has ganado")

            else:
                print ("-_-")
                user_number = int(input("Ultimo intento: "))

                if user_number == number_to_guess:
                    print("Enhorbuena")
                else:
                    print("Penoso...")