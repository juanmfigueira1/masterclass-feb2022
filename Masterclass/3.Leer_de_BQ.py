from google.oauth2 import service_account # para generar conexion
import pandas as pd # para leer BQ
# from google.cloud import bigquery # otra opcion para interactuar con BQ pero esta libreria es de google

# Generamos conexion a BQ
def Drive_Connection():
    '''Genera la conexion con BQ'''
    bq_cred = service_account.Credentials.from_service_account_file('local/big_query.json')
    print("Esta funcion devuelve las credenciales para la conexion: 'bq_cred'")
    return bq_cred

bq_cred = Drive_Connection()

# Si queremos leer una tabla
sql = """SELECT * FROM `data-layer-vtex-apub.data_warehouse.masterclass_feb22`"""
df_bq = pd.read_gbq(sql, project_id='data-layer-vtex-apub', credentials = bq_cred, dialect='standard')
print(df_bq)

sql_ak = """SELECT * FROM `data-layer-vtex-apub.data_warehouse.masterclass_feb22` where state = 'AK'"""
df_bq_ak = pd.read_gbq(sql_ak, project_id='data-layer-vtex-apub', credentials = bq_cred, dialect='standard')
print(df_bq_ak)

sql_fecha = """SELECT * FROM `data-layer-vtex-apub.data_warehouse.masterclass_feb22` where date <= '2020-07-31'"""
df_bq_fecha = pd.read_gbq(sql_fecha, project_id='data-layer-vtex-apub', credentials = bq_cred, dialect='standard')
print(df_bq_fecha)