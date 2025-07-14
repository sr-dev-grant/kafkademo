from kafka import KafkaConsumer
from loguru import logger
import json

consumer = KafkaConsumer(
    'orders',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='order-processing',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

logger.info("Waiting for messages...")
try:
    for message in consumer:
        order = message.value
        logger.success(f"Received order: {order['order_id']} | Status: {order['status']} | Amount: ${order['amount']}")
except KeyboardInterrupt:
    logger.warning("Consumer stopped.")
except Exception as e:
    logger.error(f"Consumer error: {e}")
