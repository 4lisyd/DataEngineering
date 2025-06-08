from kafka import KafkaConsumer
import json
import psycopg2
from datetime import datetime

consumer = KafkaConsumer(
    "test-topic",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)

conn = psycopg2.connect(
    dbname="streamdb", user="postgres", password="password", host="localhost"
)
cur = conn.cursor()

for msg in consumer:
    data = msg.value
    print(f"Received: {data}")

    cur.execute(
        "INSERT INTO events (event_time, message) VALUES (%s, %s)",
        (datetime.fromisoformat(data["event_time"]), data["message"]),
    )
    conn.commit()
