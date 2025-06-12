import pandas as pd

# Ruta al archivo
ruta_excel = r"C:\Users\primo\Desktop\Ciencia de Datos\Proyectos\Lodiser\ventas.xlsx"

# Leer la tabla de ventas
ventas_df = pd.read_excel(ruta_excel)

# Calcular el total gastado por cada cliente en cada sucursal
totales = (
    ventas_df.groupby(["id_cliente", "id_sucursal"])["total_venta"]
    .sum()
    .reset_index()
)

# Para cada cliente, quedarnos con la sucursal donde más gastó
sucursal_dominante = (
    totales.sort_values(["id_cliente", "total_venta"], ascending=[True, False])
    .drop_duplicates("id_cliente")
    .rename(columns={"id_sucursal": "sucursal_dominante"})
    .loc[:, ["id_cliente", "sucursal_dominante"]]
)

# Hacemos el reemplazo de la sucursal original por la dominante
ventas_modificado = ventas_df.drop(columns="id_sucursal").merge(
    sucursal_dominante, on="id_cliente", how="left"
)

# Renombramos la columna para mantener la estructura original
ventas_modificado = ventas_modificado.rename(columns={"sucursal_dominante": "id_sucursal"})

# Reordenamos las columnas si querés mantener el mismo orden
columnas_originales = ventas_df.columns.tolist()
ventas_modificado = ventas_modificado[columnas_originales]

# Guardamos sobrescribiendo el archivo original
ventas_modificado.to_excel(ruta_excel, index=False)
