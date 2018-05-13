import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient
import ast
import json
import threading
from kombu import Producer, Connection, Consumer, exceptions, Exchange, Queue, uuid
from kombu.utils.compat import nested
import time

BROKER_CLOUD = "localhost"

producer_connection = Connection(BROKER_CLOUD)
consumer_connection = Connection(BROKER_CLOUD)
MODE = "PUSH" # PUSH or PULL

exchange = Exchange("test", type="direct")

def handle_notification(body, message):
    # receive list items
    print('Receive message from Collector')
    print (body)
    time.sleep(10)

test = Queue(name='test', exchange=exchange,
                         routing_key='test')

while 1:
    try:
        consumer_connection.ensure_connection(max_retries=1)
        with nested(Consumer(consumer_connection, queues=test,
                             callbacks=[handle_notification], no_ack=True)):
            while True:
                consumer_connection.drain_events()
    except (ConnectionRefusedError, exceptions.OperationalError):
        print('Connection lost')
    except consumer_connection.connection_errors:
        print('Connection error')
