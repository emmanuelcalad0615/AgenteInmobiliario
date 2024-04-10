from Asistente import webScraping
import re
import time
from unidecode import unidecode
import requests
from bs4 import  BeautifulSoup



class Propiedad:
    def __init__(self, tipo:str, ubicacion: str, valor: str, habitaciones: str, lavados: str, dimension: str):
        self.id: int = len(webScraping.propiedades_list)
        self.tipo: str = tipo
        self.ubicacion: str = ubicacion
        self.dimension: str = dimension
        self.valor: str = valor
        self.habitaciones: str = habitaciones
        self.lavados: str = lavados


"""
class WebScraping:
    def __int__(self):
        self.propiedades_list: list[dict] = []
        self.propiedades_dict: dict[str, str] = {}

    def extraer_propiedades(self):
        urls = {
            'Casa': 'https://listado.mercadolibre.com.co/inmuebles/casas/antioquia/propiedades_NoIndex_True#applied_filter_id%3DPROPERTY_TYPE%26applied_filter_name%3DInmueble%26applied_filter_order%3D4%26applied_value_id%3D242060%26applied_value_name%3DCasas%26applied_value_order%3D2%26applied_value_results%3D6468%26is_custom%3Dfalse',
            'Apartamento': 'https://listado.mercadolibre.com.co/inmuebles/apartamentos/antioquia/propiedades_NoIndex_True#applied_filter_id%3DPROPERTY_TYPE%26applied_filter_name%3DInmueble%26applied_filter_order%3D4%26applied_value_id%3D242062%26applied_value_name%3DApartamento%26applied_value_order%3D1%26applied_value_results%3D16959%26is_custom%3Dfalse',
            'Finca': 'https://listado.mercadolibre.com.co/inmuebles/fincas/antioquia/propiedades_NoIndex_True#applied_filter_id%3DPROPERTY_TYPE%26applied_filter_name%3DInmueble%26applied_filter_order%3D4%26applied_value_id%3D267188%26applied_value_name%3DFincas%26applied_value_order%3D3%26applied_value_results%3D7%26is_custom%3Dfalse',
            'Oficina': 'https://listado.mercadolibre.com.co/inmuebles/oficinas/antioquia/propiedades_NoIndex_True#applied_filter_id%3DPROPERTY_TYPE%26applied_filter_name%3DInmueble%26applied_filter_order%3D4%26applied_value_id%3D242067%26applied_value_name%3DOficinas%26applied_value_order%3D4%26applied_value_results%3D456%26is_custom%3Dfalse'

        }

        for tipo, url in urls.items():
            website = url
            result = requests.get(website)
            content = result.text
            soup = BeautifulSoup(content, 'lxml')
            propiedad = soup.find_all('div', class_='ui-search-result__wrapper')
            for i in propiedad:
                tipo = tipo
                ubicacion = i.find('span', class_='ui-search-item__location-label').text.strip()
                valor = i.find('div',
                               class_='ui-search-item__group__element ui-search-item__group--price-grid').text.strip()
                atributos = i.find_all('li', class_='ui-search-card-attributes__attribute')
                habitaciones = lavados = dimension = ""
                for atributo in atributos:
                    texto = atributo.text.strip()
                    if "habitaciones" in texto.lower():
                        habitaciones = texto
                    elif "baño" in texto.lower():
                        lavados = texto
                    elif "m²" in texto:
                        dimension = texto
                url = i.find('a', class_='ui-search-link__title-card ui-search-link').get('href')

                self.propiedad_dict = {
                    "id": len(self.propiedades_list),
                    "tipo": tipo,
                    "ubicacion": ubicacion,
                    "valor": valor,
                    "habitaciones": habitaciones,
                    "lavados": lavados,
                    "dimension": dimension,
                    "url": url

                }
                self.propiedades_list.append(self.propiedad_dict)
"""

class Asistente:
    def __init__(self):
        self.propiedad: Propiedad

    def mostrar_catalogo(self, propiedades: list[dict]) -> str:
        catalogo_str = ""
        for idx, propiedad in enumerate(propiedades, start=1):
            catalogo_str += f"Propiedad {idx}:\n"
            catalogo_str += f"Tipo: {propiedad.get('tipo', 'No disponible')}\n"
            catalogo_str += f"Ubicación: {propiedad.get('ubicacion', 'No disponible')}\n"
            catalogo_str += f"Valor: {propiedad.get('valor', 'No disponible')}\n"
            catalogo_str += f"Habitaciones: {propiedad.get('habitaciones', 'No disponible')}\n"
            catalogo_str += f"Lavados: {propiedad.get('lavados', 'No disponible')}\n"
            catalogo_str += f"Dimensión: {propiedad.get('dimension', 'No disponible')}\n"
            catalogo_str += f"URL: {propiedad.get('url', 'No disponible')}\n\n"
        return catalogo_str

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
        print("4. Mostrar mis propiedades")
        print("0. Salir.\n")

class Cliente:
    def __init__(self, nombre: str, asistente: Asistente, propiedad: Propiedad = None):

        self.nombre: str = nombre
        self.asistente: str = asistente
        self.propiedad: Propiedad = propiedad

    def saludar(self) -> str:
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

    def agregar_venta(self, propiedades: list[dict]) -> dict[str, str]:
        propiedad_add = {
            "id": self.propiedad.id,
            "tipo": self.propiedad.tipo,
            "ubicacion": self.propiedad.ubicacion,
            "valor": self.propiedad.valor,
            "habitaciones": self.propiedad.habitaciones,
            "lavados": self.propiedad.lavados,
            "dimension": self.propiedad.dimension
        }
        propiedades.append(propiedad_add)
        return propiedad_add

    def mostrar_propiedades_venta(self, propiedades_v: list[dict]) -> str:
        ventas_str = ""
        for idx, propiedad in enumerate(propiedades_v, start=1):
            ventas_str += f"Propiedad {idx}:\n"
            ventas_str += f"Tipo: {propiedad.get('tipo', 'No disponible')}\n"
            ventas_str += f"Ubicación: {propiedad.get('ubicacion', 'No disponible')}\n"
            ventas_str += f"Valor: {propiedad.get('valor', 'No disponible')}\n"
            ventas_str += f"Habitaciones: {propiedad.get('habitaciones', 'No disponible')}\n"
            ventas_str += f"Lavados: {propiedad.get('lavados', 'No disponible')}\n"
            ventas_str += f"Dimensión: {propiedad.get('dimension', 'No disponible')}\n"
            ventas_str += f"URL: {propiedad.get('url', 'No disponible')}\n\n"
        return ventas_str











