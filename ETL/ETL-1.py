#%%
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)

# 1. Lectura de la Información:
#    - Leer los archivos CSV (ventas.csv, productos.csv, clientes.csv).
#    - Explorar los conjuntos de datos para comprender su estructura, columnas, tipos de datos, etc.
#%%
df_ventas = pd.read_csv('ventas.csv', index_col=0)
df_ventas

df_productos = pd.read_csv('productos.csv', index_col=0, error_bad_lines=False, warn_bad_lines=False)
df_productos

df_clientes = pd.read_csv('clientes.csv', index_col=0)
df_clientes

#%%
# Información de dataframe
# # def info_df(df_ventas):
#     info = df_ventas.info()
#     print(f'Con la info vemos los nombres de las columnas, los nulos y los tipos de datos: {info}')
#     estadistcas = df_ventas.describe()
#     print(f'Con describe vemos los parámetros estadísticos: {estadisticas}')
#     forma = df_ventas.shape
#     print(f'Cuántas filas y columnas tenemos: {forma}')
#     columnas = df_ventas.columns.to_list()
#     print(f'Las columnas que tenemos son: {columnas}')
#     nulos = df_ventas.isnull().sum() # aunque ya sale en la info
#     print(f'Los nulos por columna son: {nulos}')
#     
#
#

df_ventas['ID_Cliente'].duplicated().sum()
#%%
# 2. Transformación de Datos:
#     - Limpiar los datos: manejar valores nulos, eliminar duplicados si los hay, corregir errores tipográficos, etc.
#     - Realizar la integración de datos: unir los conjuntos de datos apropiados para obtener una tabla única que contenga información de ventas junto con detalles de productos y clientes.
#     - Aplicar transformaciones relevantes según sea necesario: por ejemplo, convertir tipos de datos, renombrar columnas, crear nuevas características derivadas, etc.