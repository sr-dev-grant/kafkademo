from kafka import KafkaProducer
from loguru import logger
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

statuses = ['created', 'paid', 'shipped', 'delivered']

def generate_event(order_id):
    return {
        'order_id': order_id,
        'amount': round(random.uniform(10, 500), 2),
        'status': random.choice(statuses)
    }

for i in range(10):
    order_id = f"ORD{i:03d}"
    event = generate_event(order_id)
    try:
        producer.send('orders', event)
        logger.info(f"Sent: {event}")
    except Exception as e:
        logger.error(f"Failed to send event: {e}")
    time.sleep(1)

producer.flush()
