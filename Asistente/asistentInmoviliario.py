from Asistente.propiedad import Propiedad
from webScraping import PropertyScraper
import re
import time
from unidecode import unidecode

scraper = PropertyScraper()

class Asistente:
    def __init__(self, property_scraper: PropertyScraper):
        self.property_scraper: PropertyScraper = property_scraper

    def mostrar_catalogo(self) -> tuple[str, list[Propiedad]] :
        catalogo_str = ""
        for idx, propiedad in enumerate(self.property_scraper.propiedades_list, start=1):
            catalogo_str += f"Propiedad {propiedad.id}:\n"
            catalogo_str += f"Tipo: {propiedad.tipo if hasattr(propiedad, 'tipo') else 'No disponible'}\n"
            catalogo_str += f"Ubicación: {propiedad.ubicacion if hasattr(propiedad, 'ubicacion') else 'No disponible'}\n"
            catalogo_str += f"Valor: {propiedad.valor if hasattr(propiedad, 'valor') else 'No disponible'}\n"
            catalogo_str += f"Habitaciones: {propiedad.habitaciones if hasattr(propiedad, 'habitaciones') else 'No disponible'}\n"
            catalogo_str += f"Lavados: {propiedad.lavados if hasattr(propiedad, 'lavados') else 'No disponible'}\n"
            catalogo_str += f"Dimensión: {propiedad.dimension if hasattr(propiedad, 'dimension') else 'No disponible'}\n"
            catalogo_str += f"URL: {propiedad.url if hasattr(propiedad, 'url') else 'No disponible'}\n\n"
        return catalogo_str, self.property_scraper.propiedades_list

    def buscar(self, tipo: str = None, ubicacion: str = None, valor_max: int = None, habitaciones_minimas: int = None, lavados_minimos: int = None, dimension_minima: int = None) -> list [Propiedad]:
        propiedades_encontradas = []
        for propiedad in self.property_scraper.propiedades_list:
            valor_int = int(propiedad.valor.replace('$', '').replace('.', ''))
            habitaciones_extraer = re.search(r"\d+", propiedad.habitaciones)
            habitaciones_int = int(habitaciones_extraer.group()) if habitaciones_extraer else 0
            lavados_extraer = re.search(r"\d+", propiedad.lavados)
            lavados_int = int(lavados_extraer.group()) if lavados_extraer else 0
            dimension_extraer = re.search(r"\d+", propiedad.dimension)
            dimension_int = int(dimension_extraer.group()) if dimension_extraer else 0

            if  (tipo is None or tipo.lower() in unidecode(propiedad.tipo.lower())) and \
                (ubicacion is None or ubicacion.lower() in unidecode(propiedad.ubicacion.lower())) and \
                (valor_max is None or valor_int <= int(valor_max))and \
                (habitaciones_minimas is None or habitaciones_int >= int(habitaciones_minimas)) and \
                (lavados_minimos is None or lavados_int >=  int(lavados_minimos)) and \
                (dimension_minima is None or dimension_int >= int(dimension_minima)):
                propiedades_encontradas.append(propiedad)

        return propiedades_encontradas

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
        print("2. Buscar propiedad.\n")
        print("3. Agregar propiedad.\n")
        print("4. Poner propiedad a la venta\n")
        print("5. Mostrar mis propiedades\n")
        print("0. Salir.\n")




