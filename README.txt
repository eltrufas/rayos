# Mapa interactivo rayos GOES12

Visualizacion interactiva de los datos de rayos del GOES12.

Incluye dos componentes:
* convert.py: Script para procesar los datos de netcdf a parquet. El script
  tambien toma las posiciones de los impactos en grados y las proyecta a Web
  Mercator
* server.py: Una aplicacion de Panel que genera la visualizacion en si

Para correr:
1. Instalar requerimientos: pip install -r requirements.txt
2. Preprocesar los datos con convert.py
3. Correr la visualizacion con "panel serve"

Tambien es posible correr los programas dentro de un contenedor usando el
Containerfile incluido


