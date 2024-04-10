from Asistente import asistentInmoviliario, webScraping

asistente = asistentInmoviliario.Asistente()
nombre = str(input("Ingrese su nombre: "))
cliente = asistentInmoviliario.Cliente(nombre, asistente)
saludo = cliente.saludar()
print(f"{saludo}")
opcion = True
propiedades_venta = []




while opcion != 0:

        asistente.mostrar_menu()
        opcion = int(input("Ingrese una de las opciones: "))



        if opcion == 1:

                catalogo = asistente.mostrar_catalogo(webScraping.propiedades_list)
                print(catalogo)



        if opcion == 2:
                tipo = str(input("Ingrese el tipo de propiedad: "))
                ubicacion = str(input("Ingrese la ubicacion de la propiedad: "))
                valor = str(input("Ingrese el valor de la propiedad : "))
                habitaciones = str(input("Ingrese la cantidad de habitaciones: "))
                lavados = str(input("Ingrese la cantidad de baños: "))
                dimesion = str(input("Ingrese la dimension de la propiedad: "))
                propiedad = asistentInmoviliario.Propiedad(tipo, ubicacion, valor, habitaciones, lavados, dimesion)
                asistente = asistentInmoviliario.Asistente()
                client1 = asistentInmoviliario.Cliente(nombre, asistente, propiedad)
                propiedad_add = client1.agregar_venta(webScraping.propiedades_list)
                propiedades_venta.append(propiedad_add)
                print(webScraping.propiedades_list[-1])

        if opcion == 3:
                requeriments = {
                        "Tipo": None,
                        "Ubicacion": None,
                        "Valor Máximo": None,
                        "Habitaciones Mínimas": None,
                        "Baños Mínimos": None,
                        "Dimension Mínima": None
                }
                for key, item in requeriments.items():
                        while True:
                                response = str(input(f"¿Desea ingresar {key} de la propiedad?. Responda 'Si' o 'No': ")).lower()
                                if response == "si":
                                        requeriments[f"{key}"] = str(input(f"Ingrese {key} de la propiedad: "))
                                        break
                                elif response.lower() == "no":
                                        requeriments[f"{key}"] = requeriments[f"{key}"]
                                        break

                                else:
                                        print("Ingrese una opción válida")




                asistente = asistentInmoviliario.Asistente()
                propiedades_encontradas= asistente.buscar(tipo= requeriments['Tipo'], ubicacion= requeriments['Ubicacion'], valor_max= requeriments['Valor Máximo'], habitaciones_minimas= requeriments['Habitaciones Mínimas'], lavados_minimos= requeriments['Baños Mínimos'], dimension_minima= requeriments['Dimension Mínima'])
                for idx, propiedad  in enumerate(propiedades_encontradas, start= 1):
                        print(f"\nPropieda {idx}\n"
                              f"Tipo: {propiedad.get('tipo', 'No disponible')}\n"
                              f"Ubicacion: {propiedad.get('ubicacion', 'No disponible')}\n"
                              f"Valor: {propiedad.get('valor', 'No disponible')}\n"
                              f"Habitaciones: {propiedad.get('habitaciones', 'No disponible')}\n"
                              f"Baños: {propiedad.get('lavados', 'No disponible')}\n"
                              f"Dimension: {propiedad.get('dimension', 'No disponible')}\n")

        if opcion == 4:
                venta_str = cliente.mostrar_propiedades_venta(propiedades_venta)
                print(venta_str)















