import pandas as pd # para leer el csv anterior en la carpeta local
from google.oauth2 import service_account # para generar conexion con BigQuery
import pandas_gbq # para interactuar con BQ

# Primero, con Pandas, leemos el csv generado anteriormente
df = pd.read_csv('local/Bajadas/df_covid_por_estado.csv')

# Generamos conexion a BQ
def Drive_Connection():
    '''Genera la conexion con BQ'''
    bq_cred = service_account.Credentials.from_service_account_file('local/big_query.json')
    print("Esta funcion devuelve las credenciales para la conexion: 'bq_cred'")
    return bq_cred

bq_cred = Drive_Connection()

# Enviamos el df a BQ - Podemos crear o reemplazar una tabla
pandas_gbq.to_gbq(df, 'data_warehouse.masterclass_feb22', project_id= 'masterclass-python-bigquery', if_exists= 'replace', credentials = bq_cred)

# Si queremos anexar datos de una tabla en lugar de reemplazar
pandas_gbq.to_gbq(df, 'data_warehouse.masterclass_feb22', project_id= 'masterclass-python-bigquery', if_exists= 'append', credentials = bq_cred)




