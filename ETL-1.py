
# 1. Lectura de la Información:
#    - Leer los archivos CSV (ventas.csv, productos.csv, clientes.csv).
#    - Explorar los conjuntos de datos para comprender su estructura, columnas, tipos de datos, etc.

#%%
# df_ventas = pd.read_csv('ventas.csv', index_col=0)
# df_ventas

# df_productos = pd.read_csv('productos.csv', index_col=0, error_bad_lines=False, warn_bad_lines=False)
# df_productos

# df_clientes = pd.read_csv('clientes.csv', index_col=0)
# df_clientes


#%%
# Información de dataframe
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
def leer_csv(archivo,index_col=0):
    df = pd.read_csv(archivo, index_col=0, error_bad_lines=False, warn_bad_lines=False)
    

    # if num_col == 0:
    #     df = pd.read_csv(archivo, index_col=0)
    # else:
    #     dataframe = pd.read_csv(archivo,usecols=range(num_col),index_col=0)
    # return dataframe


def exploracion_df(df):
     
    print(f'Con la info vemos los nombres de las columnas, los nulos y los tipos de datos: {df.info()}')
    
    print(f'Con describe vemos los parámetros estadísticos: {df.describe()}')
    
    print(f'Cuántas filas y columnas tenemos: {df.shape}')
   
    print(f'Las columnas que tenemos son: {df.columns.to_list()}')

    print(f'Los nulos por columna son: {df.isnull().sum()}')

    print(f'Los duplicados por columna son: {df.duplicated().sum()}')

    

#%%
df_clientes = leer_csv("clientes.csv")

exploracion_df(df_clientes)

#%%
# 2. Transformación de Datos:
#     - Limpiar los datos: manejar valores nulos, eliminar duplicados si los hay, corregir errores tipográficos, etc.
#     - Realizar la integración de datos: unir los conjuntos de datos apropiados para obtener una tabla única que contenga información de ventas junto con detalles de productos y clientes.
#     - Aplicar transformaciones relevantes según sea necesario: por ejemplo, convertir tipos de datos, renombrar columnas, crear nuevas características derivadas, etc.



# %%
