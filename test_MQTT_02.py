import subprocess
import time
import datetime

import paho.mqtt.client as mqtt     # MQTTのライブラリをインポート

MQTT_TOPIC = 'home_IoT/watering_system'

# ブローカーに接続できたときの処理
def on_connect(client, userdata, flag, rc):
    print('[test_MQTT.py] Connected with result code ' + str(rc))  # 接続できた旨表示
    client.subscribe(MQTT_TOPIC, 1)  # subするトピックを設定 

# ブローカーが切断したときの処理
def on_disconnect(client, userdata, flag, rc):
    if  rc != 0:
        print('Unexpected disconnection.')
        
def on_message(client, userdata, msg):
    # メッセージ受け取り
    get_msg = msg.payload.decode('utf-8')
    print(get_msg)


# MQTTの接続設定
client = mqtt.Client()                 # クラスのインスタンス(実体)の作成
client.tls_set("/home/pi/Documents/watering_system/mqtt.beebotte.com.pem")
client.username_pw_set("token:token_egIy11cZsQCilvSa") 
client.connect("mqtt.beebotte.com", 8883, 60)

client.on_connect = on_connect         # 接続時のコールバック関数を登録
client.on_disconnect = on_disconnect   # 切断時のコールバックを登録
client.on_message = on_message         # メッセージ到着時のコールバック

# client.loop_start()
while True:
    client.loop_start()
    temp = subprocess.getoutput('vcgencmd measure_temp')
    client.publish(MQTT_TOPIC, temp)
    time.sleep(10)
    client.loop_stop()
