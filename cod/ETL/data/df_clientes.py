# 1. Lectura de la Información:
#    - Leer los archivos CSV (ventas.csv, productos.csv, clientes.csv).
#    - Explorar los conjuntos de datos para comprender su estructura, columnas, tipos de datos, etc.

#%%

import pandas as pd
import numpy as np

def exploracion_csv(archivo):

    df = pd.read_csv(archivo,index_col=0)

    print("Primeras filas:")
    display(df.head(10))
    print("-----------------------------")

    print("Últimas filas:")
    display(df.tail(10))
    print("-----------------------------")

    print("Filas aleatorias:")
    display(df.sample(10))
    print("-----------------------------")

    print("El df tiene {df.shape[0]} filas y {df.shape[1]} columnas")
    print("-----------------------------")

    print("Características columnas númericas:")
    display(df.describe().T)
    print("-----------------------------")

    print("Características columnas de texto")
    display(df.describe (include='object').T)
    print("-----------------------------")

    print("Duplicados:")
    display(df.duplicated().sum())
    print("-----------------------------")

    print("Los nulos que tenemos en el conjunto de datos son:")
    df_nulos = pd.DataFrame(df.isnull().sum() / df.shape[0] * 100, columns = ["%_nulos"])
    display(df_nulos[df_nulos["%_nulos"] > 0])

    print("\n ..................... \n")
    print("Los valores que tenemos para las columnas categóricas son: ")
    df_categoricas = df.select_dtypes(include = "O")
    
    for col in df_categoricas.columns:
        print(f"La columna {col.upper()} tiene las siguientes valores únicos:")
        display(pd.DataFrame(df[col].value_counts()/df[col].shape[0])*100) 

    return pd.read_csv(archivo,index_col=0)


df_clientes = exploracion_csv("clientes.csv")
#%%
# 2. Transformación de Datos:
#     - Limpiar los datos: manejar valores nulos, eliminar duplicados si los hay, corregir errores tipográficos, etc.
#     - Realizar la integración de datos: unir los conjuntos de datos apropiados para obtener una tabla única que contenga información de ventas junto con detalles de productos y clientes.
#     - Aplicar transformaciones relevantes según sea necesario: por ejemplo, convertir tipos de datos, renombrar columnas, crear nuevas características derivadas, etc.

#%%
# Convertir los nombres de las columnas a minúsculas
df_clientes.columns = [columna.lower() for columna in df_clientes.columns]

#Corregir los nulos de las columnas que lo admitan
df_clientes['country'] = df_clientes['country'].fillna('Spain')

df_clientes['gender'] = df_clientes['gender'].fillna('Unknown')

df_clientes['address'] = df_clientes['address'].fillna('Unknown')

df_clientes['email'] = df_clientes['email'].fillna('Unknown')

df_clientes['city'] = df_clientes['city'].fillna('Unknown')






# %%
def exploracion_csv(archivo):

    df = pd.read_csv(archivo,index_col=0)

    print("Primeras filas:")
    display(df.head(10))
    print("-----------------------------")

    print("Últimas filas:")
    display(df.tail(10))
    print("-----------------------------")

    print("Filas aleatorias:")
    display(df.sample(10))
    print("-----------------------------")

    print("El df tiene {df.shape[0]} filas y {df.shape[1]} columnas")
    print("-----------------------------")

    print("Características columnas númericas:")
    display(df.describe().T)
    print("-----------------------------")

    print("Características columnas de texto")
    display(df.describe (include='object').T)
    print("-----------------------------")

    print("Duplicados:")
    display(df.duplicated().sum())
    print("-----------------------------")

    print("Los nulos que tenemos en el conjunto de datos son:")
    df_nulos = pd.DataFrame(df.isnull().sum() / df.shape[0] * 100, columns = ["%_nulos"])
    display(df_nulos[df_nulos["%_nulos"] > 0])

    print("\n ..................... \n")
    print("Los valores que tenemos para las columnas categóricas son: ")
    df_categoricas = df.select_dtypes(include = "O")
    
    for col in df_categoricas.columns:
        print(f"La columna {col.upper()} tiene las siguientes valores únicos:")
        display(pd.DataFrame(df[col].value_counts()/df[col].shape[0])*100) 

    return pd.read_csv(archivo,index_col=0)

df_ventas = exploracion_csv("ventas.csv")

# Convertir los nombres de las columnas a minúsculas
df_ventas.columns = [columna.lower() for columna in df_ventas.columns]
df_ventas


# %%
df_clientes
# %%
df_ventas

# %%
df_productos = pd.read_csv('productos.csv', index_col=0, error_bad_lines=False, warn_bad_lines=False)
df_productos
# %%
# Convertir los nombres de las columnas a minúsculas
df_productos.columns = [columna.lower() for columna in df_productos.columns]




# Ordenar las columnas

orden = ['id', 'nombre_producto', 'categoría' ,'precio', 'origen', 'descripción']
df_productos = df_productos[orden]

# %%

df_productos.index
# %%
