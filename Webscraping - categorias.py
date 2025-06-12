import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0'}

categorias_urls = {
    'chocolatería': 'https://lodiser.com.ar/chocolateria/',
    'heladería': 'https://lodiser.com.ar/heladeria/',
    'pastelería': 'https://lodiser.com.ar/pasteleria/'
}

productos = []

for categoria, main_url in categorias_urls.items():
    try:
        res_main = requests.get(main_url, headers=headers)
        soup_main = BeautifulSoup(res_main.text, 'html.parser')
        product_links = soup_main.find_all('a', class_='liquid-overlay-link z-index-3')
        product_urls = list(set([a['href'] for a in product_links if a.has_attr('href')]))
        print(f"[{categoria}] Total de URLs de productos encontradas: {len(product_urls)}")
    except Exception as e:
        print(f"[{categoria}] Error al obtener URLs de productos: {e}")
        continue

    for prod_url in product_urls:
        try:
            res = requests.get(prod_url, headers=headers)
            soup = BeautifulSoup(res.text, 'html.parser')

            nombre_tag = soup.find('h2', class_='ld-fh-element')
            nombre = nombre_tag.text.strip() if nombre_tag else 'No encontrado'

            productos.append({
                'nombre': nombre,
                'categoría': categoria
            })
        except Exception as e:
            print(f"[{categoria}] Error al procesar producto {prod_url}: {e}")

# Crear DataFrame
df_productos = pd.DataFrame(productos)

# Exportar a Excel sin índice
df_productos.to_excel('productos_por_categoria.xlsx', index=False)
