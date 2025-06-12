import pandas as pd
import numpy as np

# Cargar archivo detalle_venta
ruta_excel = r"C:\Users\primo\Desktop\Ciencia de Datos\Proyectos\Lodiser\detalle_venta.xlsx"
df_detalle = pd.read_excel(ruta_excel)

# Calcular total por venta
df_ventas_total = df_detalle.groupby("id_venta")["subtotal"].sum().reset_index()
df_ventas_total.rename(columns={"subtotal": "total_venta"}, inplace=True)

# Generar columnas adicionales
cantidad_ventas = df_ventas_total.shape[0]

# ID de cliente entre 1 y 50
df_ventas_total["id_cliente"] = np.random.randint(1, 51, size=cantidad_ventas)

# ID de sucursal entre 1 y 4
df_ventas_total["id_sucursal"] = np.random.randint(1, 5, size=cantidad_ventas)

# Medio de pago ponderado
medios_pago = ["Efectivo", "Débito", "Crédito", "Transferencia"]
probabilidades = [0.1, 0.2, 0.3, 0.4]
df_ventas_total["medio_pago"] = np.random.choice(medios_pago, p=probabilidades, size=cantidad_ventas)

# Generar fechas aleatorias entre 01/01/2025 y 30/04/2025
fechas_disponibles = pd.date_range(start="2025-01-01", end="2025-04-30")
fechas_finales = np.random.choice(fechas_disponibles, size=cantidad_ventas)
df_ventas_total["fecha"] = sorted(fechas_finales)

# Reordenar columnas
df_ventas_total = df_ventas_total[["id_venta", "fecha", "id_sucursal", "id_cliente", "total_venta", "medio_pago"]]

# Mostrar una muestra y exportar a Excel
print(df_ventas_total.head())
df_ventas_total.to_excel("ventas.xlsx", index=False)
