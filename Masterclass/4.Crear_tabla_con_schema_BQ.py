from google.oauth2 import service_account # para generar conexion con BigQuery
from google.cloud import bigquery # otra opcion para interactuar con BQ pero esta libreria es de google

# Generamos conexion a BQ
def Drive_Connection():
    '''Genera la conexion con BQ'''
    bq_cred = service_account.Credentials.from_service_account_file('local/big_query.json')
    print("Esta funcion devuelve las credenciales para la conexion: 'bq_cred'")
    return bq_cred

bq_cred = Drive_Connection()


# Crear una tabla vacía en BQ, definiendo el esquema con la libreria y API de google.
client = bigquery.Client(project='data-layer-vtex-apub',credentials=bq_cred)
project = client.project
dataset_ref = bigquery.DatasetReference(project, 'data_warehouse')
table_ref = dataset_ref.table("masterclass_feb22_test")

schema = [
    bigquery.SchemaField("date", "TIMESTAMP", mode="NULLABLE"),
    bigquery.SchemaField("state", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("positive", "FLOAT", mode="NULLABLE"),
    bigquery.SchemaField("probableCases", "FLOAT", mode="NULLABLE"),
    bigquery.SchemaField("negative", "FLOAT", mode="NULLABLE"),
    bigquery.SchemaField(
        "detalle",
        "RECORD",
        mode="REPEATED",
        fields=[
            bigquery.SchemaField("status", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("address", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("city", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("state", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("zip", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("numberOfYears", "STRING", mode="NULLABLE")
        ]
        )
    ]

table = bigquery.Table(table_ref, schema=schema)
table = client.create_table(table)  # API request


