import json
from ...config.main import get_config,get_app
from confluent_kafka import Producer
app = get_app()
config = get_config()

def create_kafka_producer():
    conf = {'bootstrap.servers': config['KAFKA_URI']}
    app.producer = Producer(conf)

def send_message(message):
    serialized_message = json.dumps(message).encode('utf-8')
    app.producer.produce(config['TOPIC'], value=serialized_message)
    app.producer.flush()

def close_producer():
    app.producer.flush()
    app.producer.close()