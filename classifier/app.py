import os
import json
from kafka import KafkaConsumer, KafkaProducer

import pickle
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TRANSACTIONS_TOPIC = os.environ.get("TRANSACTIONS_TOPIC")
PREDICT_TOPIC = os.environ.get("PREDICT_TOPIC")

with open('model_knn.pkl', 'rb') as model_pkl:
	knn = pickle.load(model_pkl)

def predict_iris2(transaction: dict):
    # Read value from message
    sl = transaction["sepal length"]
    sw = transaction["sepal width"]
    pl = transaction["petal length"]
    pw = transaction["petal width"]
    new_record = np.array([[sl, sw, pl, pw]])
    # get the prediction
    predict_result = knn.predict(new_record)
     
    if predict_result.size == 1: 
        return predict_result.item(0)
    else:
        return None


if __name__ == "__main__":
    consumer = KafkaConsumer(
        TRANSACTIONS_TOPIC,
        bootstrap_servers=KAFKA_BROKER_URL,
        value_deserializer=lambda value: json.loads(value),
    )
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        value_serializer=lambda value: json.dumps(value).encode(),
    )

    for message in consumer:
        transaction: dict = message.value
        result = predict_iris2(transaction)
        transaction['predicted'] = result #add to message
        producer.send(PREDICT_TOPIC, value=transaction)
        print(transaction, result)  # DEBUG
