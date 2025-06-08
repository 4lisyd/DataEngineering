from kafka import KafkaProducer
import json
import time
from datetime import datetime
import random

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

while True:
    msg = {
        "event_time": datetime.utcnow().isoformat(),
        "message": f"Random number: {random.randint(0, 100)}",
    }
    producer.send("test-topic", msg)
    print(f"Sent: {msg}")
    time.sleep(1)
