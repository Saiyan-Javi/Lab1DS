import pandas as pd

# Cargar el archivo Excel
archivo_excel = "C:\\Users\\Javier Chiquin\\OneDrive\\Documents\\UVG\\Cuarto año\\Segundo Semestre\\Data Science\\Archivos Lab1\\IMPORTACIONES.xlsx"  # Reemplaza con la ruta de tu archivo
df = pd.read_excel(archivo_excel)

# Mostrar las primeras filas del DataFrame
print(df.head())