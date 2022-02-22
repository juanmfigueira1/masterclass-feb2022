# Objetivo: Vamos a leer el DF anterior, vamos a crear la conexión con BigQuery y vamos a enviar este DF a Bigquery


# Primero, con Pandas, leemos el csv generado anteriormente
import pandas as pd
df = pd.read_csv('local/Bajadas/df_covid_por_estado.csv')


# Generamos conexion a BQ
from google.oauth2 import service_account # para generar conexion con BigQuery
bq_cred = service_account.Credentials.from_service_account_file('local/big_query.json')
bq_cred


# Enviamos el df a BQ - Podemos crear o reemplazar una tabla
import pandas_gbq # para interactuar con BQ

pandas_gbq.to_gbq(df, 'data_warehouse.masterclass_feb22', project_id= 'masterclass-python-bigquery', if_exists= 'replace', credentials = bq_cred)

# Si queremos anexar datos de una tabla en lugar de reemplazar
pandas_gbq.to_gbq(df, 'data_warehouse.masterclass_feb22', project_id= 'masterclass-python-bigquery', if_exists= 'append', credentials = bq_cred)




