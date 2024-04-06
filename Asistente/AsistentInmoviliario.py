from Asistente import webScraping


class Propiedad:
    def __init__(self, tipo:str, ubicacion: str, valor: int, habitaciones: int, lavados: int, dimension: int):
        self.id: int = len(webScraping.propiedades_list)
        self.tipo: str = tipo
        self.ubicacion: str = ubicacion
        self.dimension: int = dimension
        self.valor: int = valor
        self.habitaciones: int = habitaciones
        self.lavados: int = lavados
class Asistente:
    def __init__(self):
        self.propiedad: Propiedad


    def mostrar_catalogo(self):
        for idx, propiedad in enumerate(webScraping.propiedades_list, start=1):
            print(f"Propiedad {idx}:")
            print(f"Tipo: {propiedad.get('tipo', 'No disponible')}")
            print(f"Ubicación: {propiedad.get('ubicacion', 'No disponible')}")
            print(f"Valor: {propiedad.get('valor', 'No disponible')}")
            print(f"Habitaciones: {propiedad.get('habitaciones', 'No disponible')}")
            print(f"Lavados: {propiedad.get('lavados', 'No disponible')}")
            print(f"Dimensión: {propiedad.get('dimension', 'No disponible')}")
            print(f"URL: {propiedad.get('url', 'No disponible')}")
            print()

    def propiedad_venta(self, propiedad: Propiedad):
        propiedad_add={
            "id": propiedad.id,
            "tipo": propiedad.tipo,
            "ubicacion": propiedad.ubicacion,
            "valor": propiedad.valor,
            "habitaciones": propiedad.habitaciones,
            "lavados": propiedad.lavados,
            "dimension": propiedad.dimension
        }
        webScraping.propiedades_list.append(propiedad_add)

    def buscar(self, propiedad: Propiedad):
        pass

class Cliente:
    def __int__(self, nombre: str):
        self.nombre: str = nombre

    def saludar(self, nombre: str):
        pass


