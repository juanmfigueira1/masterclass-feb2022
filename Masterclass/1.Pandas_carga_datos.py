import pandas as pd


# Importar datos de COVID de la web con Pandas
df = pd.read_csv('https://api.covidtracking.com/v1/states/daily.csv')
df.head()


# Vemos que info hay
df.shape
df.info()


# Convertimos date a formato Date
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
df['date'] # Si seleccionamos una sola columna devuelve una serie en lugar de un DataFrame


# Recorremos el DataFrame
df.iloc[0,:] # con iloc podemos movernos en el dataframe por posiciones. al seleccionar una sola fila y/o columna devuelve una serie en lugar de DF
df.iloc[:,0] # trae todas las filas para la primera columna con la estructura de Serie
df.iloc[0:5,-1] # trae las 5 1ras filas para la ultima columna con la estructura de Serie
state_AK = df['state']=='AK' # Trae todos los registros en que el estado sea AK
state_AK
df[state_AK]
df.columns


# Agregamos un campo o columna nueva
df['letalidad'] = df['death'] / df['positive']
df.columns

# Podemos generar una tabla pivot
import numpy as np
pd.pivot_table(df, values='letalidad', index=['date'],
                    columns=['state'], aggfunc=np.mean)


# Elegimos quedarnos con algunas columnas
df.describe()
estadistica = df.describe()

cols_2_use = ['date','state']

serie_means = estadistica.iloc[1]
serie_means

mayor_a_0 =serie_means>0 # al seleccionar una sola fila devuelve una serie. Identificamos las que tienen mean > 0
mayor_a_0
serie_means[mayor_a_0]
serie_means[mayor_a_0].index
serie_means[mayor_a_0].index.to_list()

cols_2_use.extend(serie_means[mayor_a_0].index.to_list())
cols_2_use
df = df[cols_2_use]
print(df.head())


# Guardamos el DF generado
df.to_csv('local/Bajadas/df_covid_por_estado.csv', index=False) # en este caso lo guardamos en nuestra carpeta local






