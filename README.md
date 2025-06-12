# 🧪 Generación y Análisis de Datos Simulados para Lodiser S.A.

Este proyecto fue desarrollado con el objetivo de simular un entorno de análisis comercial para **Lodiser S.A.**, una empresa argentina del rubro alimenticio especializada en la producción de chocolates, helados y pastelería. El proyecto abarca desde la recolección de información desde la web, la generación de bases de datos sintéticas, el modelado de datos en SQL, y la construcción de un tablero ejecutivo en **Power BI**.

## 🧰 Herramientas utilizadas

- Python (pandas, numpy, sqlalchemy, openpyxl, requests, BeautifulSoup)
- Jupyter Notebook
- SQLite (a través de SQLAlchemy)
- Power BI (incluyendo medidas DAX personalizadas)
- Excel

## 🧾 Estructura del proyecto

### 1. 🕸️ Web Scraping
Se extrajo información desde el sitio web de Lodiser para estructurar categorías, productos, sucursales y recetas:

- [`Webscraping - Productos.py`](./Webscraping%20-%20Productos.py)
- [`Webscraping - productos descripciones.py`](./Webscraping%20-%20productos%20descripciones.py)
- [`Webscraping - categorias.py`](./Webscraping%20-%20categorias.py)
- [`Webscraping - sucursales.py`](./Webscraping%20-%20sucursales.py)
- [`Webscraping - Recetas.py`](./Webscraping%20-%20Recetas.py)
- [`Webscraping - recetas completas.py`](./Webscraping%20-%20recetas%20completas.py)

### 2. 🏗️ Generación de bases de datos sintéticas
Se generaron datos simulados para el primer cuatrimestre del año 2025, incluyendo clientes, ventas y detalle de ventas. Para esta etapa se utilizaron herramientas como **NumPy** y **Pandas** para crear datos aleatorios realistas y consistentes:

- [`Generación tabla_clientes.py`](./Generación%20tabla_clientes.py)
- [`Generación tabla ventas.py`](./Generación%20tabla%20ventas.py)
- [`Generación tabla detalle_ventas.py`](./Generación%20tabla%20detalle_ventas.py)
- [`Modificación tabla ventas - corrección sucursal-cliente.py`](./Modificación%20tabla%20ventas%20-%20corrección%20sucursal-cliente.py)

### 3. 🗃️ Modelado en base de datos
Todos los datos fueron integrados en una base de datos relacional utilizando **SQLite** mediante **SQLAlchemy** como ORM:

- [`lodiser.db`](./lodiser.db)
- [`Carga base de datos a sqlite.py`](./Carga%20base%20de%20datos%20a%20sqlite.py)

### 4. 🔍 Análisis y refinamiento de datos
Se utilizó **Jupyter Notebook** para realizar un análisis exploratorio y aplicar modificaciones basadas en criterios comerciales y demográficos, con el objetivo de dotar a la base de datos de mayor verosimilitud y coherencia analítica:

- [`lodiser.ipynb`](./lodiser.ipynb)

### 5. 📊 Desarrollo de Dashboard en Power BI
Se diseñó un tablero ejecutivo interactivo en **Power BI**, aplicando medidas personalizadas en **DAX**, filtros contextuales y criterios visuales alineados con la identidad de marca de Lodiser. El diseño prioriza la claridad, el acceso rápido a insights clave y una estética profesional:

- [`lodiser dashboard.pbix`](./lodiser%20dashboard.pbix)

#### Página 1 - Reporte Ejecutivo
- Ventas totales y cantidad de ventas
- Facturación por cliente, por producto, por sucursal
- Análisis temporal de ventas (por mes)
- Segmentadores: sucursal, mes, categoría de producto

#### Página 2 - Análisis Producto a Producto
- Métricas individuales por producto
- Imagen destacada del producto y nombre de la marca
- Segmentadores: sucursal, mes, categoría de producto

## 📂 Archivos adicionales

- [`productos.xlsx`](./productos.xlsx)
- [`clientes.xlsx`](./clientes.xlsx)
- [`detalle_ventas.xlsx`](./detalle_ventas.xlsx)
- [`ventas.xlsx`](./ventas.xlsx)
- [`sucursales.xlsx`](./sucursales.xlsx)
- [`recetas.xlsx`](./recetas.xlsx)

## 🎯 Objetivo del proyecto

Este proyecto busca demostrar competencias clave para un rol de **Analista de Datos**, tales como:

- Automatización y extracción de datos desde la web
- Generación de datos sintéticos coherentes y con sentido comercial
- Modelado de base de datos relacional con SQLAlchemy
- Análisis y refinamiento de datos en Python
- Diseño de dashboards ejecutivos con Power BI y DAX
- Comunicación visual efectiva y alineación estética con identidad de marca

---

📩 Para cualquier consulta o colaboración, no dudes en contactarme.
