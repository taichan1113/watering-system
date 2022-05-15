import os
from dotenv import load_dotenv
import paho.mqtt.client as mqtt

from service import ServiceConductor as service

load_dotenv('./.env')
BEEBOTTE_TOKEN = os.getenv('BEEBOTTE_TOKEN')
MQTT_TOPIC_SERVER = 'home_IoT/watering_system_server'
MQTT_TOPIC_DEVICE = 'home_IoT/watering_system_device'

def on_connect(client, userdata, flag, rc):
    print('[test_MQTT.py] Connected with result code ' + str(rc))
    client.subscribe(MQTT_TOPIC_DEVICE, 1) 

def on_disconnect(client, userdata, flag, rc):
    if  rc != 0:
        print('Unexpected disconnection.')

def on_message(client, userdata, msg):
    get_msg = msg.payload.decode('utf-8')
    print(get_msg)
    service_conductor = service.ServiceConductor(get_msg)
    service_conductor.conduct_service()
    client.publish(MQTT_TOPIC_SERVER, service_conductor.publish_message)

# MQTTの接続設定
client = mqtt.Client()
client.tls_set("/home/pi/Documents/watering_system/mqtt.beebotte.com.pem")
client.username_pw_set(f'token:{BEEBOTTE_TOKEN}')
client.connect("mqtt.beebotte.com", 8883, 60)

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.loop_start()
