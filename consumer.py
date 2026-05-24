import json
from kafka import KafkaConsumer
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

client = InfluxDBClient(
    url="http://localhost:8086",
    token="mytoken123",
    org="factory"
)
write_api = client.write_api(write_options=SYNCHRONOUS)

consumer = KafkaConsumer(
    'sensor-data',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Waiting for sensor data...")

for message in consumer:
    data = message.value
    point = (Point("sensor_reading")
             .tag("machine_id", data["machine_id"])
             .field("temperature", data["temperature"])
             .field("vibration", data["vibration"])
             .field("pressure", data["pressure"]))
    write_api.write(bucket="sensors", record=point)
    print(f"Saved: {data['machine_id']} | temp={data['temperature']} | vibration={data['vibration']} | pressure={data['pressure']}")