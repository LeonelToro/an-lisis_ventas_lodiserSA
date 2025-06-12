import pandas as pd
import random

def generar_cuit():
    tipo = random.choice([20, 27, 30])
    dni = random.randint(20000000, 39999999)
    verificador = random.randint(0, 9)
    return f"{tipo}-{dni}-{verificador}"

def generar_telefono():
    prefijos_fijos = ['011', '0341', '0291', '0381', '0221', '0351', '0261']
    prefijo = random.choice(prefijos_fijos)
    numero = random.randint(2000000, 9999999)
    return f"{prefijo}-{numero}"

provincias = [
    "Buenos Aires", "Córdoba", "Santa Fe", "Mendoza"
]

ciudades = {
    "Buenos Aires": ["La Plata", "Mar del Plata", "Quilmes", "Bahía Blanca"],
    "Córdoba": ["Córdoba", "Villa Carlos Paz", "Río Cuarto", "Alta Gracia"],
    "Santa Fe": ["Rosario", "Santa Fe", "Rafaela"],
    "Mendoza": ["Mendoza", "San Rafael", "Godoy Cruz", "Luján de Cuyo"],
}

# Lista ampliada con 50 nombres únicos
nombres_base = [
    "La Fiorentina", "Dolce Gelato", "Postres del Valle", "Cremas Nórdicas",
    "Tentaciones", "El Obrador", "Dulce & Frío", "La Dulcería", "San Benito",
    "Cremas del Oeste", "Sabores del Alma", "Dulce Patagonia", "Gelato Argento",
    "Cielo de Vainilla", "La Casa del Helado", "Rincón del Dulce", "Don Gelato",
    "Frigorífico del Sabor", "La Estación", "Lácteos Norte", "Postres Artesanales",
    "Helados del Centro", "Confitería Roma", "Nieve Mía", "Sabor Andino", "Helados Milán",
    "Santa Crema", "Nube Helada", "Nórdico", "Copito de Nieve", "El Tacho",
    "Amalfi", "Polar", "Confitería Olimpo", "Gelato Sur", "Nevado",
    "El Poste", "Frío Azul", "Helados Ancla", "Sabores Reales", "Heladería París",
    "Dulcinea", "Helados Lucía", "Nevadito", "Delizia", "Tentazione",
    "Aurora", "Helados Tita", "Postre y Arte", "La Toscana", "El Manjar"
]

razones_sociales = [f"{random.choice(['Heladería', 'Confitería', 'Dulces', 'Sabores'])} {nombre}" 
                    for nombre in random.sample(nombres_base, 50)]

lista_ciudad = []
lista_provincia = []
for _ in range(50):
    prov = random.choice(provincias)
    ciudad = random.choice(ciudades[prov])
    lista_provincia.append(prov)
    lista_ciudad.append(ciudad)

clientes = pd.DataFrame({
    "id_cliente": range(1, 51),
    "CUIT": [generar_cuit() for _ in range(50)],
    "razón_social": razones_sociales,
    "ciudad": lista_ciudad,
    "provincia": lista_provincia,
    "contacto": [generar_telefono() for _ in range(50)]
})

clientes.to_excel("clientes_completo.xlsx", index=False)
