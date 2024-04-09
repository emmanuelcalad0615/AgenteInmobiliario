from Asistente import webScraping
import re
import time


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


    def __str__(self) -> str:
        catalogo_str = ""
        for idx, propiedad in enumerate(webScraping.propiedades_list, start=1):
            catalogo_str += f"Propiedad {idx}:\n"
            catalogo_str += f"Tipo: {propiedad.get('tipo', 'No disponible')}\n"
            catalogo_str += f"Ubicación: {propiedad.get('ubicacion', 'No disponible')}\n"
            catalogo_str += f"Valor: {propiedad.get('valor', 'No disponible')}\n"
            catalogo_str += f"Habitaciones: {propiedad.get('habitaciones', 'No disponible')}\n"
            catalogo_str += f"Lavados: {propiedad.get('lavados', 'No disponible')}\n"
            catalogo_str += f"Dimensión: {propiedad.get('dimension', 'No disponible')}\n"
            catalogo_str += f"URL: {propiedad.get('url', 'No disponible')}\n\n"
        return catalogo_str

    def propiedad_venta(self, propiedad: Propiedad) :
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


    def buscar(self):
        pass



class Cliente:
    def __init__(self, nombre: str):
        self.nombre: str = nombre

    def __str__(self) -> str:
        casa = (
            "░░░░░░░░░░░░░░░░▄▓▄░░░\n"
            "░░░░▄█▄░░░░░░░░▄▓▓▓▄░░\n"
            "░░▄█████▄░░░░░▄▓▓▓▓▓▄░\n"
            "░▀██┼█┼██▀░░░▄▓▓▓▓▓▓▓▄\n"
            "▄▄███████▄▄▄▄▄▄▄▄█▄▄▄▄\n"
        )
        mensaje = f"{self.nombre}"



        return (f"{casa}\n"
                f"Hola, {self.nombre}. Bienvenido a PropietyFinder, estoy a tus servicios.")

    def mostrar_menu(self):
        menu = (" __  __              __  \n"
                "|  \/  |            /_/  \n"
                "| \  / | ___ _ __  _   _ \n"
                "| |\/| |/ _ \ '_ \| | | |\n"
                "| |  | |  __/ | | | |_| |\n"
                "|_|  |_|\___|_| |_|\__,_|\n")
        time.sleep(1.5)
        print(f"{menu}\n")
        time.sleep(1.5)
        print("1. Mostrar catálogo.\n")
        print("2. Poner propiedad a la venta.\n")
        print("3. Buscar propiedad.\n")
        print("0. Salir.\n")





