import os
import pandas as pd
from sqlalchemy import create_engine

# Carpeta donde están los archivos y la base SQLite
folder_path = r"C:\Users\primo\Desktop\Ciencia de Datos\Proyectos\Lodiser"
db_path = os.path.join(folder_path, "lodiser.db")

# Crear motor de SQLAlchemy para SQLite
engine = create_engine(f"sqlite:///{db_path}")

# Mapear archivos Excel a nombres de tablas SQL
excel_to_table = {
    "productos.xlsx": "productos",
    "recetas.xlsx": "recetas",
    "sucursales.xlsx": "sucursales",
    "clientes.xlsx": "clientes",
    "detalle_ventas.xlsx": "detalle_ventas",
    "ventas.xlsx": "ventas"
}

for file_name, table_name in excel_to_table.items():
    file_path = os.path.join(folder_path, file_name)
    print(f"Cargando {file_name} a tabla {table_name}...")

    # Leer Excel
    df = pd.read_excel(file_path)

    # Guardar en SQLite (reemplaza tabla si existe)
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"{table_name} cargada con {len(df)} registros.")

print("Carga completada.")
