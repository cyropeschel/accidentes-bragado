Accidentes Bragado

Proyecto de análisis de datos sobre accidentes de tránsito en la ciudad de Bragado, Argentina.
Desarrollado en Python utilizando Pandas y Matplotlib para el procesamiento y visualización de datos.

Objetivo del proyecto:
El objetivo es analizar datos de accidentes para obtener información útil como:
 - Vehículos más involucrados
 - Zonas más peligrosas
 - Horarios con más accidentes
 - Condiciones climáticas en los accidentes
 - Cantidad de heridos
 - Días de la semana con mayor siniestralidad

Tecnologías utilizadas:
 - Python
 - Pandas
 - Matplotlib
 - NumPy
 - Git & GitHub

Estructura del proyecto
Accidentes Bragado/
│
├── prueba.py              # Código principal de análisis
├── accidentes.csv         # Dataset de accidentes


El proyecto incluye:
Limpieza de datos
 - Eliminación de espacios
 - Conversión de fechas y horas
 - Normalización de textos
Estadísticas:
 - Conteo de vehículos involucrados
 - Accidentes por clima
 - Accidentes por zona
 - Heridos por accidente
 - Accidentes por día de la semana
 - Accidentes por hora
Visualizaciones:
 - Gráfico de vehículos
 - Top zonas más peligrosas
 - Accidentes por clima
 - Heridos por accidente
 - Heatmap (día vs hora)

Ejemplo de análisis:
vehiculos = pd.concat([df["vehiculo1"], df["vehiculo2"]]).value_counts()
print(vehiculos)

Posibles mejoras futuras:
 - Dashboard web con Flask
 - Mapa interactivo de accidentes 
 - Análisis predictivo con Machine Learning
 - Base de datos en lugar de CSV

Autor:
Proyecto desarrollado por Cyro Peschel

Notas:
Este proyecto es con fines educativos y de práctica en análisis de datos con Python.
El dataset utilizado es simulado para fines de práctica y aprendizaje
