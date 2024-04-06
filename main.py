from Asistente import AsistentInmoviliario


propiedad_1 = AsistentInmoviliario.Propiedad(tipo="Casa", ubicacion="Medellín", valor=200000000, habitaciones=3, lavados=2, dimension=150)


asistente = AsistentInmoviliario.Asistente()


asistente.propiedad_venta(propiedad_1)
asistente.mostrar_catalogo()
