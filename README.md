REQUIRES python3.11

activate pyenv

(kafkademo) grant@fedora kafkademo % docker-compose up -d

Create kafka topic:

(kafkademo) grant@fedora kafkademo % docker exec -it kafkademo-kafka-1 \
kafka-topics --create \
--topic orders \
--bootstrap-server localhost:9092 \
--partitions 1 \
--replication-factor 1

Created topic orders.

python consumer.py

python producer.py

grant@fedora venv % docker exec -it kafkademo-kafka-1 \
/usr/bin/kafka-console-consumer \
--bootstrap-server localhost:9092 \
--topic orders \
--from-beginning

{"order_id": "ORD000", "amount": 134.12, "status": "shipped"}
{"order_id": "ORD001", "amount": 38.97, "status": "paid"}
{"order_id": "ORD002", "amount": 208.65, "status": "delivered"}
{"order_id": "ORD003", "amount": 95.31, "status": "paid"}
{"order_id": "ORD004", "amount": 357.46, "status": "created"}
{"order_id": "ORD005", "amount": 201.95, "status": "shipped"}
{"order_id": "ORD006", "amount": 451.1, "status": "shipped"}
{"order_id": "ORD007", "amount": 27.25, "status": "created"}
{"order_id": "ORD008", "amount": 499.51, "status": "shipped"}
{"order_id": "ORD009", "amount": 347.08, "status": "paid"}