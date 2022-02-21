from re import X
import pandas as pd


# Importar datos de COVID de la web con Pandas (https://covidtracking.com/data/api)
df = pd.read_csv('https://api.covidtracking.com/v1/states/daily.csv')


# Vemos que info hay
df.head()
df.columns
df.shape
df.info()
df.describe() # resumen de las variables numericas


# Ordenar datos
df
df.sort_values(by='date', ascending=True) # inplace = True si queremos que esto afecte al DF
df


# Cambiamos formatos
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
df['date'] # Si seleccionamos una sola columna devuelve una serie en lugar de un DataFrame

df['state'] = df['state'].astype('string')
df.info()

# Recorremos el DataFrame
df.iloc[0,:] # con iloc podemos movernos en el dataframe por posiciones. al seleccionar una sola fila y/o columna devuelve una serie en lugar de DF
df.iloc[:,0] # trae todas las filas para la primera columna con la estructura de Serie
df.iloc[0:5,-1] # trae las 5 1ras filas para la ultima columna con la estructura de Serie


# Aplicamos un filtro
state_AK = df['state']=='AK' # Trae todos los registros en que el estado sea AK
state_AK
df[state_AK]

state_list = ['AK','AR','AS']
df[df['state'].isin(state_list)]


# Agregamos un campo o columna nueva
df['letalidad'] = df['death'] / df['positive']
df.columns

# Podemos generar una tabla pivot
import numpy as np
pd.pivot_table(df, values='letalidad', index=['date'],
                    columns=['state'], aggfunc=np.mean)


# Ejemplo funcion
def funcion_masterclass(nro):
    x = nro**2 + nro*3 + 1
    return x

funcion_masterclass(2)


# Suponiendo que necesitaramos quedarnos solo con las columnas del DataFrame con mean >0
df.describe() # resumen de las variables numericas
estadistica = df.describe()

cols_2_use = ['date','state'] # partimos de estas columnas no numericas pero que igual las queremos
df[cols_2_use]

estadistica
serie_means = estadistica.iloc[1]
serie_means

mayor_a_0 =serie_means>0 # al seleccionar una sola fila devuelve una serie. Identificamos las que tienen mean > 0
mayor_a_0
serie_means[mayor_a_0]
serie_means[mayor_a_0].index
serie_means[mayor_a_0].index.to_list()

cols_2_use
cols_2_use.extend(serie_means[mayor_a_0].index.to_list())
cols_2_use
df = df[cols_2_use]
df


# Guardamos el DF generado
df.to_csv('local/Bajadas/df_covid_por_estado.csv', index=False) # en este caso lo guardamos en nuestra carpeta local






