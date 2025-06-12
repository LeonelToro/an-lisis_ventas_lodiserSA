import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL objetivo
url = "https://lodiser.com.ar/contacto/"

# User-Agent para evitar bloqueos
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    print("✅ Conexión exitosa al sitio web.")
except Exception as e:
    print(f"❌ Error al conectar con la web: {e}")
    exit()

try:
    soup = BeautifulSoup(response.content, "html.parser")
    section = soup.find("section", {"id": "company"})
    if not section:
        raise ValueError("Sección con ID 'company' no encontrada.")
    print("✅ Sección de tiendas localizada.")
except Exception as e:
    print(f"❌ Error al analizar el HTML: {e}")
    exit()

# Lista donde almacenamos los datos
datos_tiendas = []

# Extraer cada tienda desde las columnas
columns = section.find_all("div", class_="vc_column-inner")
print(f"🔍 Cantidad de bloques de tiendas encontrados: {len(columns)}")

for col in columns:
    tienda = {
        "nombre": "no encontrado",
        "dirección": "no encontrado",
        "ciudad": "no encontrado",
        "mail": "no encontrado",
        "telefono": "no encontrado",
        "telefono2": "no encontrado"
    }

    try:
        contents = col.find("div", class_="contents")
        if not contents:
            continue

        # Nombre
        nombre_tag = contents.find("h3")
        if nombre_tag:
            tienda["nombre"] = nombre_tag.get_text(strip=True)

        # Datos dentro del párrafo
        p_tag = contents.find("p")
        if p_tag:
            spans = p_tag.find_all("span", class_="list-iconbox")
            telefonos_encontrados = []

            for span in spans:
                texto = span.get_text(strip=True)

                if "@" in texto:
                    tienda["mail"] = texto
                elif texto.lower().startswith("whatsapp"):
                    telefonos_encontrados.append(texto)
                elif texto.startswith("+") or texto.replace(" ", "").replace("-", "").isdigit():
                    telefonos_encontrados.append(texto)
                elif any(kw in texto for kw in ["C.A.B.A", "Buenos Aires", "Av.", "Calle", "–", "Capital Federal"]):
                    tienda["dirección"] = texto
                    # Suponemos que la ciudad está al final de la dirección, por ejemplo: "... – C.A.B.A"
                    if "–" in texto:
                        partes = texto.split("–")
                        tienda["ciudad"] = partes[-1].strip()

            # Asignar teléfonos si se encontraron
            if len(telefonos_encontrados) > 0:
                tienda["telefono"] = telefonos_encontrados[0]
            if len(telefonos_encontrados) > 1:
                tienda["telefono2"] = telefonos_encontrados[1]

        datos_tiendas.append(tienda)
        print(f"✅ Tienda procesada: {tienda['nombre']}")
    except Exception as e:
        print(f"❌ Error procesando una tienda: {e}")

# Crear DataFrame
df = pd.DataFrame(datos_tiendas)

# Exportar a Excel
try:
    df.to_excel("tiendas_lodiser.xlsx", index=False)
    print("✅ Archivo 'tiendas_lodiser.xlsx' creado correctamente.")
except Exception as e:
    print(f"❌ Error al exportar a Excel: {e}")
