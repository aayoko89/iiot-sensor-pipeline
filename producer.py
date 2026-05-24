import json
import time
import random
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def make_sensor_reading(machine_id):
    return {
        "machine_id": machine_id,
        "temperature": round(random.uniform(60, 120), 2),
        "vibration": round(random.uniform(0.1, 5.0), 2),
        "pressure": round(random.uniform(10, 50), 2),
        "timestamp": time.time()
    }

while True:
    for machine in ["M-001", "M-002", "M-003"]:
        reading = make_sensor_reading(machine)
        producer.send('sensor-data', reading)
        print(f"Sent: {reading}")
    time.sleep(1)