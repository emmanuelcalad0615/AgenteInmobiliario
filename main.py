import time

from Asistente import asistentInmoviliario, webScraping
nombre = str(input("Ingrese su nombre: "))
cliente = asistentInmoviliario.Cliente(nombre)
saludo = cliente.__str__()
print(f"{saludo}")
opcion = True


while opcion != 0:

        cliente.mostrar_menu()
        opcion = int(input("Ingrese una de las opciones: "))



        if opcion == 1:
                asistente = asistentInmoviliario.Asistente()
                catalogo = asistente.__str__()
                print(catalogo)



        if opcion == 2:
                tipo = str(input("Ingrese el tipo de propiedad: "))
                ubicacion = str(input("Ingrese la ubicacion de la propiedad: "))
                valor = int(input("Ingrese el valor de la propiedad: "))
                habitaciones = int(input("Ingrese la cantidad de habitaciones: "))
                lavados = int(input("Ingrese la cantidad de baños: "))
                dimesion = int(input("Ingrese la dimension de la propiedad: "))
                propiedad = asistentInmoviliario.Propiedad(tipo, ubicacion, valor, habitaciones, lavados, dimesion)
                asistente = asistentInmoviliario.Asistente()
                propiedad_add = asistente.propiedad_venta(propiedad)
                print(webScraping.propiedades_list[-1])











