import os
import json
from datetime import datetime
from time import sleep
from kafka import KafkaProducer
from transactions import create_random_transaction

KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TRANSACTIONS_TOPIC = os.environ.get("TRANSACTIONS_TOPIC")
TRANSACTIONS_PER_SECOND = float(os.environ.get("TRANSACTIONS_PER_SECOND"))
SLEEP_TIME = 1 / TRANSACTIONS_PER_SECOND

print("KAFKA_BROKER_URL", KAFKA_BROKER_URL)

if __name__ == "__main__":
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        # Encode all values as JSON
        value_serializer=lambda value: json.dumps(value).encode(),
    )

    producer2 = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        # Encode all values as JSON
        value_serializer=lambda value: json.dumps(value).encode(),
    )
    counter = 0
    while True:
        if counter >= 1000:
            break
        print("     ", counter)
        transaction: dict = create_random_transaction()
        producer.send(TRANSACTIONS_TOPIC, value=transaction)
        print("TRX1", datetime.now(), transaction)  # DEBUG

        transaction2: dict = create_random_transaction()
        producer2.send(TRANSACTIONS_TOPIC, value=transaction2)
        print("TRX2", datetime.now(), transaction2)  # DEBUG
        sleep(SLEEP_TIME)
        counter += 1

        