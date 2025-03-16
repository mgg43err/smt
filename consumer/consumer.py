import os
from kafka import KafkaConsumer

KAFKA_BROKER = os.getenv("KAFKA_BROKER")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BROKER,
    auto_offset_reset="earliest",
    group_id="test_group"
)

def consume_messages():
    for message in consumer:
        print(f"Consumed: {message.value.decode('utf-8')}")

if __name__ == "__main__":
    consume_messages()
