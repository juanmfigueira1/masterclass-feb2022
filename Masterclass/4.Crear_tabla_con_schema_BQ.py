# Objetivo: vamos a conectarnos con Bigquery y desde Python vamos a crear una tabla desde cero, definiendo los schemas.


# Generamos conexion a BQ
from google.oauth2 import service_account # para generar conexion con BigQuery
bq_cred = service_account.Credentials.from_service_account_file('local/big_query.json')


# Crear una tabla vacía en BQ, definiendo el esquema con la libreria y API de google.
from google.cloud import bigquery # otra opcion para interactuar con BQ pero esta libreria es de google

client = bigquery.Client(project='masterclass-python-bigquery',credentials=bq_cred)
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


