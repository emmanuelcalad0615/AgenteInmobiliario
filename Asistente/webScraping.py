import requests
from bs4 import BeautifulSoup
website = 'https://listado.mercadolibre.com.co/inmuebles/antioquia/propiedades_NoIndex_True#applied_filter_id%3Dstate%26applied_filter_name%3DUbicación%26applied_filter_order%3D6%26applied_value_id%3DTUNPUEFOVGFiZWI3%26applied_value_name%3DAntioquia%26applied_value_order%3D1%26applied_value_results%3D29312%26is_custom%3Dfalse'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
propiedades= soup.find_all('div', class_='ui-search-result__wrapper')
propiedades_list=[]
propiedad_dict = {}
for i in propiedades:
    tipo = i.find('span', class_='ui-search-item__group__element ui-search-item__subtitle-grid').text.strip()
    ubicacion = i.find('span', class_='ui-search-item__location-label').text.strip()
    valor = i.find ('div', class_='ui-search-item__group__element ui-search-item__group--price-grid').text.strip()
    habitaciones = i.find('li', class_='ui-search-card-attributes__attribute').text.strip()
    lavados = i.find('li', class_='ui-search-card-attributes__attribute').text.strip()
    dimension = i.find('li', class_='ui-search-card-attributes__attribute').text.strip()
    url = i.find('a', class_='ui-search-link__title-card ui-search-link').get('href')


    propiedad_dict = {
        "id": len(propiedades_list),
        "tipo": tipo,
        "ubicacion": ubicacion,
        "valor": valor,
        "habitaciones": habitaciones,
        "lavados": lavados,
        "dimension": dimension,
        "url": url

    }
    propiedades_list.append(propiedad_dict)








