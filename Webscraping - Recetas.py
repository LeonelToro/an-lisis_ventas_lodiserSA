import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {
    "User-Agent": "Mozilla/5.0"
}

base_url = "https://lodiser.com.ar/recetas/"
print("Obteniendo URLs de recetas...")

res = requests.get(base_url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

# Obtener todos los enlaces de recetas
enlaces = soup.find_all('a', class_='liquid-overlay-link z-index-3')
urls = list(set([a['href'] for a in enlaces if a.get('href')]))

print(f"Se encontraron {len(urls)} recetas.\n")

resultados = []

for url in urls:
    print(f"Procesando receta: {url}")
    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # Nombre de la receta
        nombre_tag = soup.find('h1', class_='entry-title')
        nombre = nombre_tag.get_text(strip=True) if nombre_tag else 'No encontrado'
        print(f"Nombre: {nombre}")

        # Imagen principal
        try:
            img_tag = soup.find('img', class_='vc_single_image-img')
            if img_tag:
                if img_tag.has_attr('data-src'):
                    imagen = img_tag['data-src']
                elif img_tag.has_attr('src'):
                    imagen = img_tag['src']
                else:
                    imagen = 'No encontrada'
            else:
                imagen = 'No encontrada'
        except Exception:
            imagen = 'No encontrada'

        # Dificultad
        try:
            dificultad_tag = soup.find('h3', class_='lqd-iconbox-title')
            dificultad = dificultad_tag.get_text(strip=True) if dificultad_tag else 'No encontrada'
        except Exception:
            dificultad = 'No encontrada'

        # Rinde
        try:
            rinde_tag = soup.find('div', class_='ld-fh-element')
            rinde = rinde_tag.get_text(strip=True) if rinde_tag else 'No encontrado'
        except Exception:
            rinde = 'No encontrado'

        # Preparación
        try:
            preparacion_div = soup.find('div', class_='recetas-instrucciones')
            pasos = preparacion_div.find_all('li') if preparacion_div else []
            preparacion = ' '.join([li.get_text(strip=True) for li in pasos])
        except Exception:
            preparacion = 'No encontrada'

        # Ingredientes concatenados
        ingredientes_texto = ''
        try:
            h3_ingredientes = soup.find('h3', string=lambda t: t and 'ingredientes' in t.lower())
            if h3_ingredientes:
                tbody = h3_ingredientes.find_next('tbody')
                filas = tbody.find_all('tr')
                lista_ingredientes = []
                for fila in filas:
                    columnas = fila.find_all('td')
                    if len(columnas) == 2:
                        ingrediente = columnas[0].get_text(strip=True)
                        cantidad = columnas[1].get_text(strip=True)
                        lista_ingredientes.append(f"- {ingrediente}: {cantidad}.")
                ingredientes_texto = '\n'.join(lista_ingredientes)
                print(f"Se extrajeron {len(lista_ingredientes)} ingredientes.\n")
            else:
                print("No se encontró el bloque de ingredientes.\n")
        except Exception as e:
            print(f"Error al extraer ingredientes: {e}\n")

        resultados.append({
            'nombre': nombre,
            'url': url,
            'imagen': imagen,
            'dificultad': dificultad,
            'rinde': rinde,
            'ingredientes': ingredientes_texto if ingredientes_texto else 'No encontrados',
            'preparacion': preparacion
        })

        time.sleep(1)

    except Exception as e:
        print(f"Error general con {url}: {e}\n")

# Guardar en Excel
df = pd.DataFrame(resultados)
df.to_excel("recetas_lodiser_concatenado.xlsx", index=False)
print("Exportación completada: recetas_lodiser_concatenado.xlsx")
