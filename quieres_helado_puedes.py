quieres_helado_input = input("Quieres un helado? (Si / No)").upper()
tienes_dinero_input = input("Tienes dinero? (Si / No)").upper()

if quieres_helado_input == "SI" and tienes_dinero_input == "SI":
    print("Perfecto, ve a por uno")
elif quieres_helado_input and not tienes_dinero_input:
    print("Pues ves a buscar dinero")
elif tienes_dinero_input and not quieres_helado_input:
    print("Entonces compramelo a mi")
else:
    print("Pues nada -_-")