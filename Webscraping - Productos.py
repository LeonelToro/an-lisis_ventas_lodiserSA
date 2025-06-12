import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {'User-Agent': 'Mozilla/5.0'}
main_url = 'https://lodiser.com.ar/productos/'

# Obtener URLs de productos
try:
    res_main = requests.get(main_url, headers=headers)
    soup_main = BeautifulSoup(res_main.text, 'html.parser')
    product_links = soup_main.find_all('a', class_='liquid-overlay-link z-index-3')
    product_urls = list(set([a['href'] for a in product_links if a.has_attr('href')]))
    print(f"Total de URLs de productos encontradas: {len(product_urls)}")
except Exception as e:
    print(f"Error al obtener URLs de productos: {e}")
    product_urls = []

exclusiones = ['mailto:', 'Casa Central', 'Productos', 'Chocolatería', 'Heladería']
productos = []

for i, prod_url in enumerate(product_urls):
    try:
        res = requests.get(prod_url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')

        nombre_tag = soup.find('h2', class_='ld-fh-element')
        nombre = nombre_tag.text.strip() if nombre_tag else 'No encontrado'

        img_prod_tag = soup.find('img', class_='wp-post-image')
        imagen_producto = img_prod_tag['src'] if img_prod_tag else 'No encontrada'

        marca_img_tag = soup.find('img', class_='alignnone')
        imagen_marca = marca_img_tag['src'] if marca_img_tag else 'No encontrada'

        descripcion = 'No encontrada'
        sabores = 'No encontrados'

        # Buscar contenido dentro del div de descripción
        desc_div = soup.find('div', class_='woocommerce-product-details__short-description')
        if desc_div:
            parrafos = desc_div.find_all('p')
            for p in parrafos:
                texto = p.get_text(strip=True)
                if not texto:
                    continue
                if 'Sabores' in texto:
                    sabores = texto.replace('Sabores', '').strip()
                elif descripcion == 'No encontrada':
                    descripcion = texto.strip()
        else:
            print(f"[Warning] No se encontró div de descripción en: {prod_url}")

        productos.append({
            'nombre': nombre,
            'url': prod_url,
            'imagen_producto': imagen_producto,
            'imagen_marca': imagen_marca,
            'descripcion': descripcion,
            'sabores': sabores
        })
        print(f"[{i+1}/{len(product_urls)}] Procesado: {nombre}")
        time.sleep(1)

    except Exception as e:
        print(f"Error procesando {prod_url}: {e}")

# Guardar CSV
try:
    df_productos = pd.DataFrame(productos)
    df_productos.to_csv('productos_lodiser_limpio.csv', index=False, encoding='utf-8-sig')
    print("Archivo CSV guardado correctamente.")
except Exception as e:
    print(f"Error al guardar CSV: {e}")

