## Objetivo: importar un dataset, entender qué datos hay, crear una nueva columna, analizarla y guardarlo.

import pandas as pd


# Importar datos de COVID de la web con Pandas (https://covidtracking.com/data/api)
df = pd.read_csv('https://api.covidtracking.com/v1/states/daily.csv')
df

# Vemos que info hay
df.head()
df.columns
df.shape
df.info()
df.describe() # resumen de las variables numericas


# Ordenar datos
df
df.sort_values(by='date', ascending=True) # inplace = True si queremos que esto afecte al DF


# Cambiamos formatos
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
df['date'] # Si seleccionamos una sola columna devuelve una serie en lugar de un DataFrame

df['state'] = df['state'].astype('string')
df.info()


# Aplicamos un filtro
df['state']

state_AK = df['state']=='AK' # Trae todos los registros en que el estado sea AK
state_AK
df[state_AK]


# Agregamos un campo o columna nueva
df['letalidad'] = df['death'] / df['positive']
df.columns


# Podemos generar una tabla pivot
pd.pivot_table(df, values='letalidad', index=['date'],
                    columns=['state'], aggfunc='mean')


# Guardamos el DF generado
df.to_csv('local/Bajadas/df_covid_por_estado.csv', index=False) # en este caso lo guardamos en nuestra carpeta local






