quiere_helado_input = input("Te apetece un helado? (Sí / No)").upper()

if quiere_helado_input == "SI":
    quiere_helado = True
elif quiere_helado_input == "NO":
    quiere_helado = False
else:
    print("Te he dicho que digas si o no, nada mas, así que me lo tomare como un no")
    quiere_helado = False


tiene_dinero_input = input("Tienes dinero para un helado? (Sí / No)").upper()
señor_helado_input = input("Está el señor de los helados? (Sí / No)").upper()
tu_tia_input = input("Tu tia te puede pagar el helado? (Sí / No)").upper()

tiene_dinero = tiene_dinero_input == "SI"
tu_tia = tu_tia_input == "SI"

quiere_helado = quiere_helado_input == "SI"
puede_permitirselo = tiene_dinero or tu_tia
señor_helado = señor_helado_input == "SI"



if quiere_helado and puede_permitirselo and señor_helado:
    print("Entonces cometelo")
else:
    print("Pues nada")

