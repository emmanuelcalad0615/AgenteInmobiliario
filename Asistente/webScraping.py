import requests
from bs4 import  BeautifulSoup

from Asistente.propiedad import Propiedad


class PropertyScraper:
    def __init__(self):
        self.propiedades_list: list[Propiedad] = []
        self.urls: dict[str] = {
            'Casa': 'https://listado.mercadolibre.com.co/inmuebles/casas/antioquia/propiedades_NoIndex_True#applied_filter_id%3DPROPERTY_TYPE%26applied_filter_name%3DInmueble%26applied_filter_order%3D4%26applied_value_id%3D242060%26applied_value_name%3DCasas%26applied_value_order%3D2%26applied_value_results%3D6468%26is_custom%3Dfalse',
            'Apartamento': 'https://listado.mercadolibre.com.co/inmuebles/apartamentos/antioquia/propiedades_NoIndex_True#applied_filter_id%3DPROPERTY_TYPE%26applied_filter_name%3DInmueble%26applied_filter_order%3D4%26applied_value_id%3D242062%26applied_value_name%3DApartamento%26applied_value_order%3D1%26applied_value_results%3D16959%26is_custom%3Dfalse',
            'Finca': 'https://listado.mercadolibre.com.co/inmuebles/fincas/antioquia/propiedades_NoIndex_True#applied_filter_id%3DPROPERTY_TYPE%26applied_filter_name%3DInmueble%26applied_filter_order%3D4%26applied_value_id%3D267188%26applied_value_name%3DFincas%26applied_value_order%3D3%26applied_value_results%3D7%26is_custom%3Dfalse',
            'Oficina': 'https://listado.mercadolibre.com.co/inmuebles/oficinas/antioquia/propiedades_NoIndex_True#applied_filter_id%3DPROPERTY_TYPE%26applied_filter_name%3DInmueble%26applied_filter_order%3D4%26applied_value_id%3D242067%26applied_value_name%3DOficinas%26applied_value_order%3D4%26applied_value_results%3D456%26is_custom%3Dfalse'
        }


    def scrape_properties(self) -> list[Propiedad]:
        for tipo, url in self.urls.items():
            website = url
            result = requests.get(website)
            content = result.text
            soup = BeautifulSoup(content, 'lxml')
            propiedad = soup.find_all('div', class_='ui-search-result__wrapper')
            for i in propiedad:
                id: int = len(self.propiedades_list)
                tipo = tipo
                ubicacion = i.find('span', class_='ui-search-item__location-label').text.strip()
                valor = i.find('div', class_='ui-search-item__group__element ui-search-item__group--price-grid').text.strip()
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


                obj_propiedad: Propiedad = Propiedad(id,tipo, ubicacion, valor, habitaciones, lavados, dimension, url)
                self.propiedades_list.append(obj_propiedad)
        return self.propiedades_list

