Entradas = ["Pan con ajo","Chuco","Piña"]
PreciosEntradas = [3.25,4.70,3.20]

PlatosFuertes = ["Sopa","Hamburguesa","Pizza"]
PreciosPlatosFuertes = [4.60, 1.99, 2.50]

Postres = ["Flan","Bombon","Tres leches"]
PreciosPostres = [3.25, 0.50, 4.50]

print("Bienvenidos a los pollos hermanos")
print("Menu")
print("------")
print("\nEntradas: ")
for i in range (len(Entradas)):
    print(f"{i+1}. {Entradas[i] } - $ {PreciosEntradas[i] } ")

print("---------")
print("\nPlatos fuertes: ")
for i in range (len(PlatosFuertes)):
    print(f"{i+4}. {PlatosFuertes[i] } - $ {PreciosPlatosFuertes[i] } ")

print("-------")
print("\nPostres: ")
for i in range (len(Postres)):
    print(f"{i+7}. {Postres[i] } - $ {PreciosPostres[i] } ")

NumPersonas = int(input("Ingrese el numero de personas que desean ordenar: "))


Total = 0
for i in range (NumPersonas):

    Nombre = input(f"Ingrese el nombre de la persona que va a ordenar para la orden {i+1} ")
    print(f"Orden numero {i+1} para la persona {Nombre} ")

    SeguirOrdenando = True
    

    while SeguirOrdenando:

        entrada = input("Por favor ingrese la entrada que desea pedir del 1 al 3 (Presione 's' para salir):  ")

        plato_fuerte = input("Por favor ingrese su plato fuerte que desea pedir del 4 al 6 (Presione 's' para salir): ")

        postre = input("Por favor ingrese su postre que desea pedir del 7 al 9 (Presione 's' para salir) ")

        if entrada == "s" or plato_fuerte == "s" or postre =="s":
            SeguirOrdenando = False
        
        if entrada == "1":
            Total = Total + PreciosEntradas[0]
        elif entrada == "2":
            Total = Total + PreciosEntradas[1]
        elif entrada == "3":
            Total = Total + PreciosEntradas[2]
        else:
            print("La opcion no existe")

        if plato_fuerte == "4":
            Total = Total + PreciosPlatosFuertes[0]
        elif plato_fuerte == "5": 
            Total = Total + PreciosPlatosFuertes[1]
        elif plato_fuerte == "6":
            Total = Total + PreciosPlatosFuertes[2]
        else:
            print("La opcion no existe")

        if postre == "7":
            Total = Total + PreciosPostres[0]
        elif postre == "8":
            Total = Total + PreciosPostres[1]
        elif postre == "9":
            Total = Total + PreciosPostres[2]
        else:
            print("La opcion no existe")
        

print(f"Gracias por su compra, el total a pagar es de {Total:.2f} ")
    



    




    