import os
from time import sleep
from kafka import KafkaProducer

KAFKA_BROKER = os.getenv("KAFKA_BROKER")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")

producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER)

def produce_messages():
    for i in range(10):
        message = f"Message {i}"
        producer.send(KAFKA_TOPIC, value=message.encode("utf-8"))
        print(f"Produced: {message}")
        sleep(2)

if __name__ == "__main__":
    produce_messages()
