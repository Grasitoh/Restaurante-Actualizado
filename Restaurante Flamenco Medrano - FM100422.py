#Preguntar para cuantas personas va a ordenar

print("Bienvenido al Restaurante GrasitoLandia")
print("Menú")
print("--------------------")
print("Entradas:")
print("1. Pan con Ajo - $4.50")
print("2. Nachos Imperial - $6.70")
print("3. Alitas Buffalo - $6.99")
print("--------------------")
print("Platos Fuertes:")
print("4. Hot Dog - $5.00")
print("5. Torta - $3.40")
print("6. Orden de tacos - $5.75")
print("--------------------")
print("Postres:")
print("7. Tartaleta - $3.90")
print("8. Flan Campero - $2.10")
print("9. Budin - $4.10")

Num_Personas = int(input("Ingrese el numero de personas a ordenar: "))

for i in range (Num_Personas):
    nombre = input(f"Ingrese el nombre de la persona para la orden {i+1} ")
    print(f"orden para la persona {i+1} ")

    Seguir_Ordenando = True
    Total = 0 

    while Seguir_Ordenando:
        Entrada = input("Por favor seleccione una entrada 1-3 (Presione s para salir): ")
        PlatoFuerte = input("Por favor ingresa un plato fuerte 4-6 (Presione s para salir): ")
        Postre = input("Por favor  ingresa un postre 7-9 (Presione s para salir): ")

        if Entrada == "s" or PlatoFuerte == "s" or Postre == "s":
            Seguir_Ordenando = False 

        if Entrada == "1":
            Total = Total + 4.50
        elif Entrada == "2":
            Total = Total + 6.70
        elif Entrada == "3":
            Total = Total + 6.99
        else:
            print("La opcion que ha seleccionado no existe, seleccione un numero del 1 al 3")
            continue

        if PlatoFuerte == "4":
            Total = Total + 5.00
        elif PlatoFuerte == "5":
            Total = Total + 3.40
        elif PlatoFuerte == "6":
            Total = Total + 5.75
        else:
            print("La opcion que ha seleccionado no existe, seleccione un numero del 4 al 6")

        if Postre == "7":
            Total = Total + 3.90
        elif Postre == "8":
            Total = Total + 2.10
        elif Postre == "9":
            Total = Total + 4.10
        else:
             print("La opcion que ha seleccionado no existe, seleccione un numero del 7 al 9")

print(f"El total a pagar es $ {Total:.2f}. Gracias por su compra ")



            

