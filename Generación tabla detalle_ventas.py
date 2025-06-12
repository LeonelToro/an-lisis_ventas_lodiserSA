import pandas as pd
import random

# Productos y precios totales (simulados previamente)
productos_data = [
    ("Pastas", 19200),
    ("Variegatos pastelería", 22000),
    ("Transfers para decorar con chocolate", 12000),
    ("Moldeo Alpino", 26000),
    ("Frutos Secos", 9500),
    ("Chocolate Tronador", 7800),
    ("Ganache", 6500),
    ("Blisters personalizados", 8000),
    ("Alfajorero Alpino", 6800),
    ("Variegatos heladería", 17600),
    ("Glucomix", 15200),
    ("Bases y Neutros", 13600),
    ("Chips Alpino", 7200),
    ("Azúcares", 8500),
    ("Mascarpone", 7800),
    ("Rellenos", 18000),
    ("Pailados", 6500),
    ("Cacao Alpino", 9000),
    ("Mixes", 19000),
    ("Baños de Heladería", 17000),
    ("Toppings", 6000),
    ("Repostero Alpino", 6800)
]

# Crear DataFrame de productos con id_producto
df_productos = pd.DataFrame(productos_data, columns=["producto", "precio_total"])
df_productos["id_producto"] = df_productos.index + 1

# Generar ventas (500 a 1000)
n_ventas = random.randint(500, 1000)
detalle_venta = []

id_detalle = 1
for id_venta in range(1, n_ventas + 1):
    productos_en_venta = random.sample(range(1, len(df_productos) + 1), random.randint(3, 10))
    for id_producto in productos_en_venta:
        cantidad = random.randint(1, 5)
        precio_unitario = df_productos.loc[df_productos["id_producto"] == id_producto, "precio_total"].values[0]
        subtotal = cantidad * precio_unitario
        detalle_venta.append([id_detalle, id_venta, id_producto, cantidad, precio_unitario, subtotal])
        id_detalle += 1

# Crear DataFrame
df_detalle_venta = pd.DataFrame(detalle_venta, columns=[
    "id_detalle", "id_venta", "id_producto", "cantidad", "precio_unitario", "subtotal"
])

df_detalle_venta.to_excel("detalle_venta.xlsx", index=False)
