import os, boto3, requests
from datetime import date

S3_BUCKET = "my-etl-bucket"
PREFIX = "nyc_taxi/raw/"
URL = "https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-01.csv"

def download_and_upload():
    local_file = "/tmp/taxi_2021-01.csv"
    r = requests.get(URL, stream=True)
    with open(local_file, "wb") as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
    s3 = boto3.client("s3")
    s3.upload_file(local_file, S3_BUCKET, PREFIX + "yellow_2021-01.csv")
    print("Uploaded to S3")

if __name__ == "__main__":
    download_and_upload()
