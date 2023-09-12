#!python3
# python 3.6

import random
import time
import json

import paho.mqtt.subscribe as subscribe
import paho.mqtt.publish as publish

broker = '127.0.0.1'
port = 1883
#base topic
main_topic = "aps"
# topic for receiving messages from ESP ECU
sub_topic = "out"


client_id = "mqtt-router"

# username = 'none'
# password = 'xxx'

def on_message(client, userdata, msg):
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    try:
        payload = json.loads(msg.payload.decode())
        #print(type(payload))
        inv = payload['inv_serial']

        inv_topic = main_topic + "/" + inv
        publish.single(topic=inv_topic, payload=msg.payload, hostname=broker, port=port, client_id=f'python-mqtt-{random.randint(0, 1000)}', keepalive=60, will=None, auth=None, tls=None)
        print("publishing  " + msg.payload.decode() + " to " + inv_topic)
    except Exception as error:
        print(f"Error {type(error).__name__} processing message: {msg.payload.decode()}")


def run():
    print("Starting MQTT Router")
    subscribe.callback(on_message, main_topic + "/" + sub_topic, hostname=broker, port=port,client_id=client_id)

if __name__ == '__main__':
    run()