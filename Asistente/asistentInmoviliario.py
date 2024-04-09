from Asistente import webScraping
import re
import time
from unidecode import unidecode


class Propiedad:
    def __init__(self, tipo:str, ubicacion: str, valor: str, habitaciones: str, lavados: str, dimension: str):
        self.id: int = len(webScraping.propiedades_list)
        self.tipo: str = tipo
        self.ubicacion: str = ubicacion
        self.dimension: str = dimension
        self.valor: str = valor
        self.habitaciones: str = habitaciones
        self.lavados: str = lavados


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


    def buscar(self, tipo: str = None, ubicacion: str = None, valor_max: int = None, habitaciones_minimas: int = None, lavados_minimos: int = None, dimension_minima: int = None) -> list [dict]:
        propiedades_encontradas = []
        for propiedad in webScraping.propiedades_list:
            valor_int = int(propiedad["valor"].replace('$', '').replace('.', ''))
            habitaciones_extraer = re.search(r"\d+", propiedad['habitaciones'])
            habitaciones_int = int(habitaciones_extraer.group()) if habitaciones_extraer else 0
            lavados_extraer = re.search(r"\d+", propiedad['lavados'])
            lavados_int = int(lavados_extraer.group()) if lavados_extraer else 0
            dimension_extraer = re.search(r"\d+", propiedad['dimension'])
            dimension_int = int(dimension_extraer.group()) if dimension_extraer else 0

            if  (tipo is None or tipo.lower() in unidecode(propiedad['tipo'].lower())) and \
                (ubicacion is None or ubicacion.lower() in unidecode(propiedad["ubicacion"].lower())) and \
                (valor_max is None or valor_int <= int(valor_max))and \
                (habitaciones_minimas is None or habitaciones_int >= int(habitaciones_minimas)) and \
                (lavados_minimos is None or lavados_int >=  int(lavados_minimos)) and \
                (dimension_minima is None or dimension_int >= int(dimension_minima)):
                propiedades_encontradas.append(propiedad)

        return propiedades_encontradas








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
        mensaje = f"Hola, {self.nombre}. Bienvenido a PropietyFinder, estoy a tus servicios."



        return (f"{casa}\n"
                f"{mensaje}")

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





