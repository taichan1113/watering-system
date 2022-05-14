import paho.mqtt.client as mqtt

from run_pump import runPump
from show_soilMoisture import humidityPercentage
from show_tempAndHumid import DHT22
from turnOn_led import ledOn

MQTT_TOPIC_SERVER = 'home_IoT/watering_system_server'
MQTT_TOPIC_DEVICE = 'home_IoT/watering_system_device'

GPIO_LED = 21

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
    if get_msg == 'service=water':
        print('test water')
        ledOn(1, GPIO_LED)
        
    elif get_msg == 'service=environment':
        print('test environment');
        sense = DHT22()
        temp = sense.get_temperature()
        hum = sense.get_humidity()
        pub_msg = f'Temperature: {temp}' + '\n' + f'Humidity: {hum}'
        print(pub_msg)
        client.publish(MQTT_TOPIC_SERVER, pub_msg)
        
    elif get_msg == 'service=stream':
        print('test stream')
        ledOn(1, GPIO_LED)
        
    else:
        ledOn(1, GPIO_LED)

# MQTTの接続設定
client = mqtt.Client()
client.tls_set("/home/pi/Documents/watering_system/mqtt.beebotte.com.pem")
client.username_pw_set("token:token_egIy11cZsQCilvSa") 
client.connect("mqtt.beebotte.com", 8883, 60)

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.loop_start()
