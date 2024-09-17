from kafka import KafkaConsumer
from influxdb_client import InfluxDBClient, Point, WritePrecision
import json

print("Starting Kafka Consumer...")

# Kafka Consumer
consumer = KafkaConsumer(
    'sensor_data',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

print("Kafka Consumer started. Connecting to InfluxDB...")

# InfluxDB Client
token = "4dzbMMlP8gKguTWo1cko0SoW222FHQ1A27lNnk09pQ1t3Xmi8OeAXg6ekqgKsNl-6tf-fOJQwCBcSv-KSHIvmA=="
org = "my-org"
bucket = "kafka-consumer"
client = InfluxDBClient(url="http://localhost:8086", token=token, org=org)
write_api = client.write_api()

print("Connected to InfluxDB. Waiting for messages...")

for message in consumer:
    data = message.value
    print(f"Received message: {data}")
    timestamp_ns = int(data['timestamp'] * 1e9)  # Convert timestamp to nanoseconds
    point = Point("sensor_data") \
        .tag("sensor_id", data['sensor_id']) \
        .field("value", data['value']) \
        .time(timestamp_ns, WritePrecision.NS)
    write_api.write(bucket=bucket, org=org, record=point)
    print(f"Written to InfluxDB: {data}")

write_api.__del__()
client.__del__()
print("Consumer finished.")
