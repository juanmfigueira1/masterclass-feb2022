from google.oauth2 import service_account # para generar conexion
import pandas as pd # para leer BQ
# from google.cloud import bigquery # otra opcion para interactuar con BQ pero esta libreria es de google

# Generamos conexion a BQ
bq_cred = service_account.Credentials.from_service_account_file('local/big_query.json')

# Si queremos leer una tabla
sql = """SELECT * FROM `masterclass-python-bigquery.data_warehouse.masterclass_feb22`"""
df_bq = pd.read_gbq(sql, project_id='masterclass-python-bigquery', credentials = bq_cred, dialect='standard') #Dialect standard: para usar BigQuery’s standard SQL dialect
print(df_bq)

sql_ak = """SELECT * FROM `masterclass-python-bigquery.data_warehouse.masterclass_feb22` where state = 'AK'"""
df_bq_ak = pd.read_gbq(sql_ak, project_id='masterclass-python-bigquery', credentials = bq_cred, dialect='standard')
print(df_bq_ak)

sql_fecha = """SELECT * FROM `masterclass-python-bigquery.data_warehouse.masterclass_feb22` where date <= '2020-07-31'"""
df_bq_fecha = pd.read_gbq(sql_fecha, project_id='masterclass-python-bigquery', credentials = bq_cred, dialect='standard')
print(df_bq_fecha)