import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0'}
urls = [
    "https://lodiser.com.ar/macarons/",
    "https://lodiser.com.ar/torta-cookies/",
    "https://lodiser.com.ar/tarta-de-pera-y-vanilla/",
    "https://lodiser.com.ar/nido-de-abejas/",
    "https://lodiser.com.ar/donas/"
]

datos_recetas = []

for url in urls:
    print(f"\n🔗 Procesando: {url}")
    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')

        # Nombre de la receta
        nombre_tag = soup.find('h2', class_='ld-fh-element')
        nombre = nombre_tag.get_text(strip=True) if nombre_tag else 'Nombre no encontrado'

        # Extraer ingredientes
        ingredientes_texto = ""
        try:
            ingredientes_secciones = soup.find_all("table", class_="recetable")
            for i, tabla in enumerate(ingredientes_secciones, 1):
                try:
                    seccion = tabla.find_previous("h3").get_text(strip=True)
                    rows = tabla.find_all("tr")
                    ingredientes = [f"- {tds[0].get_text(strip=True)}: {tds[1].get_text(strip=True)}" 
                                    for tds in [row.find_all("td") for row in rows] if len(tds) == 2]
                    ingredientes_texto += f"\n\n🟢 {seccion}:\n" + "\n".join(ingredientes)
                except Exception as e:
                    print(f"⚠️ Falló una tabla de ingredientes ({i}): {e}")
            print("✅ Ingredientes extraídos correctamente")
        except Exception as e:
            print(f"❌ Error al extraer ingredientes: {e}")
            ingredientes_texto = "Ingredientes no encontrados"

        # Extraer preparación
        preparacion_texto = ""
        try:
            secciones_preparacion = soup.find_all("ol")
            for i, lista in enumerate(secciones_preparacion, 1):
                try:
                    titulo = lista.find_previous("h3").get_text(strip=True)
                    pasos = [f"{j+1}. {li.get_text(strip=True)}" for j, li in enumerate(lista.find_all("li"))]
                    preparacion_texto += f"\n\n🔵 {titulo}:\n" + "\n".join(pasos)
                except Exception as e:
                    print(f"⚠️ Falló una sección de preparación ({i}): {e}")
            print("✅ Preparación extraída correctamente")
        except Exception as e:
            print(f"❌ Error al extraer preparación: {e}")
            preparacion_texto = "Preparación no encontrada"

        # Guardar datos
        datos_recetas.append({
            'Nombre': nombre,
            'Ingredientes': ingredientes_texto.strip(),
            'Preparación': preparacion_texto.strip(),
            'URL': url
        })

    except requests.exceptions.RequestException as e:
        print(f"❌ Error al cargar la página: {e}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

# Crear DataFrame
df = pd.DataFrame(datos_recetas)

# Exportar a Excel
df.to_excel("recetas_lodiser.xlsx", index=False)
print("\n✅ Archivo guardado como 'recetas_lodiser.xlsx'")
