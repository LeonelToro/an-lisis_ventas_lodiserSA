import pandas as pd
import requests
from bs4 import BeautifulSoup

prod1 = pd.read_excel(r"C:\Users\primo\Desktop\Ciencia de Datos\Proyectos\Lodiser\Productos para arreglar.xlsx")

headers = {'User-Agent': 'Mozilla/5.0'}
resultados = []

for url in prod1['url']:
    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')

        # Nombre del producto
        nombre_tag = soup.find('h2', class_='ld-fh-element')
        nombre = nombre_tag.get_text(strip=True) if nombre_tag else 'No encontrado'

        # Descripción completa: todos los textos dentro del div de descripción
        desc_div = soup.find('div', class_='woocommerce-product-details__short-description')
        if desc_div:
            textos = desc_div.stripped_strings
            descripcion_completa = "\n".join(textos)
        else:
            descripcion_completa = 'No encontrada'

        resultados.append({
            'url': url,
            'nombre': nombre,
            'descripcion_completa': descripcion_completa
        })

    except Exception as e:
        print(f"[Error] {url}: {e}")
        resultados.append({
            'url': url,
            'nombre': 'Error',
            'descripcion_completa': f'ERROR: {e}'
        })

# Exportar a Excel
df_resultados = pd.DataFrame(resultados)
df_resultados.to_excel('descripcion_completa_lodiser.xlsx', index=False)
print("Archivo Excel generado: descripcion_completa_lodiser.xlsx")
