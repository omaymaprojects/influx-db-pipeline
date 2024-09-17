
from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = 'sensor_data'

for i in range(10):
    data = {
        'sensor_id': f'sensor_{i}',
        'value': i * 10,
        'timestamp': time.time()
    }
    producer.send(topic, value=data)
    print(f"Sent: {data}")
    time.sleep(1)

producer.flush()
producer.close()

