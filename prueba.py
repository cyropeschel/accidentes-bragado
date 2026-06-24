import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# =========================
# CARGAR DATOS
# =========================
df = pd.read_csv(r"C:\Users\WINDOWS10\Desktop\Accidentes Bragado\accidentes.csv")
# =========================
# LIMPIEZA DE DATOS
# =========================
columnas_texto = [
    "clima",
    "vehiculo1",
    "vehiculo2",
    "zona",
    "danios1",
    "danios2",
    "hora"
]
for col in columnas_texto:
    df[col] = df[col].astype(str).str.strip()
# =========================
# CONVERSIONES NUMERICAS Y FECHAS
# =========================
df["heridos"] = pd.to_numeric(df["heridos"], errors="coerce")
df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
df["hora"] = pd.to_datetime(df["hora"], format="%H:%M", errors="coerce")
df["horas"] = df["hora"].dt.hour
df["dia_semana"] = df["fecha"].dt.day_name()
# =========================
# GRAFICO 1: VEHICULOS
# =========================
# Datos
vehiculos = pd.concat([df["vehiculo1"], df["vehiculo2"]]).value_counts()
labels = vehiculos.index
values = vehiculos.values
# Figura 2x2
fig, axs = plt.subplots(2, 2, figsize=(10, 7), layout="constrained")
# 1. Barras
axs[0, 0].bar(labels, values)
axs[0, 0].set_title("Grafico Vertical")
# 2. Línea
axs[0, 1].plot(labels, values, marker="o")
axs[0, 1].set_title("Grafico Lineal")
# 3. Circular
axs[1, 0].pie(values, labels=labels, autopct="%1.1f%%")
axs[1, 0].set_title("Grafico Circular")
# 4. Horizontal
axs[1, 1].barh(labels, values)
axs[1, 1].set_title("Grafico Horizontal")
# Bordes negros
for ax in axs.flat:
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color("black")
        spine.set_linewidth(1.5)
fig.suptitle("Vehículos involucrados en accidentes", fontsize=14)
plt.show()
# =========================
# GRAFICO 2: ZONAS TOP 5
# =========================
zonas = df["zona"].value_counts().head(5)
plt.figure(figsize=(12,6))  # Más ancho para que entren bien los nombres de las calles
plt.bar(zonas.index, zonas.values)
plt.title("Top 5 zonas más peligrosas")
plt.xticks(fontsize=9)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
# =========================
# GRAFICO 3: CLIMA
# =========================
clima = df["clima"].value_counts()
plt.bar(clima.index, clima.values)
plt.ylabel("Cantidad")
plt.title("Accidentes por clima")
plt.grid(True, axis="y", linestyle="--", alpha=0.5)
plt.show()
# =========================
# GRAFICO 4: HORAS
# =========================
df["horas"].value_counts().sort_index().plot(kind="line", marker="o")
plt.title("Accidentes por hora del día")
plt.show()
# =========================
# GRAFICO 5: HEATMAP (DIA vs HORA)
# =========================
# Dias en español
dias_es = {
    "Monday": "Lunes",
    "Tuesday": "Martes",
    "Wednesday": "Miércoles",
    "Thursday": "Jueves",
    "Friday": "Viernes",
    "Saturday": "Sábado",
    "Sunday": "Domingo"
}
df["dia_semana"] = df["fecha"].dt.day_name().map(dias_es)
# HEATMAP DATA
tabla = pd.crosstab(df["horas"], df["dia_semana"])
# Orden de los dias
orden = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
tabla = tabla.reindex(columns=orden)
# Grafico
plt.figure(figsize=(10,6))
plt.imshow(tabla, cmap="hot", aspect="auto")
plt.colorbar(label="Accidentes")
plt.xticks(range(len(tabla.columns)), tabla.columns, rotation=45)
plt.yticks(range(len(tabla.index)), tabla.index)
plt.title("Accidentes: Hora vs Día")
plt.xlabel("Día")
plt.ylabel("Hora")
plt.show()