from Asistente import asistentInmoviliario, cliente

from webScraping import PropertyScraper

scraper = PropertyScraper()
properties = scraper.scrape_properties()
asistente = asistentInmoviliario.Asistente(scraper)
nombre = str(input("Ingrese su nombre: "))
cliente = cliente.Cliente(nombre, asistente)
saludo = cliente.saludar()
print(f"{saludo}")
opcion = True
propiedades_venta = []





while opcion != 0:

        asistente.mostrar_menu()
        opcion = int(input("Ingrese una de las opciones: "))



        if opcion == 1:

                catalogo, _ = asistente.mostrar_catalogo()
                print(catalogo)



        """if opcion == 2:
                id = len()
                tipo = str(input("Ingrese el tipo de propiedad: "))
                ubicacion = str(input("Ingrese la ubicacion de la propiedad: "))
                valor = str(input("Ingrese el valor de la propiedad : "))
                habitaciones = str(input("Ingrese la cantidad de habitaciones: "))
                lavados = str(input("Ingrese la cantidad de baños: "))
                dimesion = str(input("Ingrese la dimension de la propiedad: "))
                propiedad = asistentInmoviliario.Propiedad(tipo, ubicacion, valor, habitaciones, lavados, dimesion)
                asistente = asistentInmoviliario.Asistente()
                client1 = cliente.Cliente(nombre, asistente, propiedad)
                propiedad_add = client1.agregar_venta(properties)
                propiedades_venta.append(propiedad_add)
                print(properties[-1])"""

        if opcion == 2:
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




                asistente = asistentInmoviliario.Asistente(scraper)
                propiedades_encontradas= asistente.buscar(tipo= requeriments['Tipo'], ubicacion= requeriments['Ubicacion'], valor_max= requeriments['Valor Máximo'], habitaciones_minimas= requeriments['Habitaciones Mínimas'], lavados_minimos= requeriments['Baños Mínimos'], dimension_minima= requeriments['Dimension Mínima'])
                for idx, propiedad  in enumerate(propiedades_encontradas, start= 1):
                        print(f"Propiedad {propiedad.id}:\n"
                              f"Tipo: {propiedad.tipo if hasattr(propiedad, 'tipo') else 'No disponible'}\n"
                              f"Ubicación: {propiedad.ubicacion if hasattr(propiedad, 'ubicacion') else 'No disponible'}\n"
                              f"Valor: {propiedad.valor if hasattr(propiedad, 'valor') else 'No disponible'}\n"
                              f"Habitaciones: {propiedad.habitaciones if hasattr(propiedad, 'habitaciones') else 'No disponible'}\n"
                              f"Baños:{propiedad.lavados if hasattr(propiedad, 'lavados') else 'No disponible'}\n"
                              f"Dimension: {propiedad.dimension if hasattr(propiedad, 'dimension') else 'No disponible'}\n"
                              f"URL: {propiedad.url if hasattr(propiedad, 'url') else 'No disponible'}\n\n")

        """if opcion == 4:
                venta_str = cliente.mostrar_propiedades_venta(propiedades_venta)
                print(venta_str)"""

        if opcion == 3:
                tipo = str(input("Ingrese el tipo de propiedad: "))
                ubicacion = str(input("Ingrese la ubicacion: "))
                dimension = str(input("Ingrese la dimension: "))
                valor = str(input("Ingrese el valor: "))
                habitaciones = str(input("Ingrese el número de habitaciones: "))
                lavados = str(input("Ingrese el número de baños: "))
                validacion = str(input("¿Desea Ingresar URL?: "))
                url = ""
                if validacion.lower() == "si":
                        url = str(input("Ingrese el URL"))
                elif validacion.lower() == "no":
                        url = "No disponible"

                else:
                        print("Ingrese una opción válida")

                cliente.agregar_propiedad(tipo, ubicacion, dimension, valor, habitaciones, lavados, url)

        if opcion == 4:
                id = int(input("Ingrese el ID"))
                cliente.poner_venta(id)

        if opcion == 5:
                propiedades, propiedades_list = cliente.mostrar_propiedades_cliente()
                print(propiedades)

