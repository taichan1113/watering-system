import subprocess
import time
import datetime

import paho.mqtt.client as mqtt

MQTT_TOPIC_SERVER = 'home_IoT/watering_system_server'
MQTT_TOPIC_DEVICE = 'home_IoT/watering_system_device'

def on_connect(client, userdata, flag, rc):
    print('[test_MQTT.py] Connected with result code ' + str(rc))  # 接続できた旨表示
    client.subscribe(MQTT_TOPIC_DEVICE, 1)  # subするトピックを設定 

def on_disconnect(client, userdata, flag, rc):
    if  rc != 0:
        print('Unexpected disconnection.')

def on_message(client, userdata, msg):
    get_msg = msg.payload.decode('utf-8')
    # service logic here
    print(get_msg)
    temp = subprocess.getoutput('vcgencmd measure_temp')
    client.publish(MQTT_TOPIC_SERVER, temp)


# MQTTの接続設定
client = mqtt.Client()
client.tls_set("/home/pi/Documents/watering_system/mqtt.beebotte.com.pem")
client.username_pw_set("token:token_egIy11cZsQCilvSa") 
client.connect("mqtt.beebotte.com", 8883, 60)

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.loop_start()
