import random
import pandas as pd
ciudades_colombia = ["Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena"]

tipos_propiedad = ["Casa", "Apartamento", "Finca", "Lote", "Local comercial"]

comodidades = ["Patio trasero", "Garaje/Parqueadero", "Terraza", "Piscina", "Jardín"]

estado = ("compra", "arriendo")


propiedades_venta= [
    {
        "tipo": random.choice(tipos_propiedad),
        "ubicacion": random.choice(ciudades_colombia),
        "dimension": f"{random.randint(50, 500)} m2",
        "valor": f"${random.randint(10000000, 100000000)}",
        "espacios_interiores": random.randint(1, 5),
        "comodidades": random.sample(comodidades, random.randint(1, len(comodidades))),
        "estado": random.choice(estado)
    }
    for i in range(10000)
]
dp = pd.DataFrame(propiedades_venta)