import boto3, psycopg2, tempfile
import pandas as pd

S3_BUCKET = "my-etl-bucket"
KEY = "candlestick/curated/"

def load():
    s3 = boto3.client("s3")
    objs = s3.list_objects_v2(Bucket=S3_BUCKET, Prefix=KEY)
    for obj in objs.get("Contents", []):
        if obj["Key"].endswith(".parquet"):
            with tempfile.NamedTemporaryFile(suffix=".parquet") as tmp:
                s3.download_file(S3_BUCKET, obj["Key"], tmp.name)
                df = pd.read_parquet(tmp.name)
                conn = psycopg2.connect(
                    dbname="airflow", user="airflow", password="airflow", host="postgres"
                )
                cur = conn.cursor()
                for _, row in df.iterrows():
                    cur.execute(
                        "INSERT INTO taxi_trips (pickup_dt, dropoff_dt, passenger_count) VALUES (%s,%s,%s)",
                        (row.pickup_dt, row.dropoff_dt, row.passenger_count),
                    )
                conn.commit()
                cur.close()
                conn.close()
    print("Loaded to Postgres")

if __name__ == "__main__":
    load()
