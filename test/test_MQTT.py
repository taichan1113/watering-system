import subprocess
import time
import datetime

import paho.mqtt.client as mqtt     # MQTTのライブラリをインポート
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

import RPi.GPIO as GPIO
from DHT11_Python import dht11
from on_led import ledOn

# global variable
GPIO_LED = 21
GPIO_TEMP_HUMID = 14

# DHTT
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
sensor = dht11.DHT11(pin=GPIO_TEMP_HUMID)

# line bot
MY_CHANNEL_ACCESS_TOKEN = '1t7brnNPKRUXdMZt7jm1R9TcWeJXW8vWsnBH46ZLwotcQqvxEjgcxt1JiR18aUE+6bSNMfyANbN90kps4cQHmISYgTXSzBnAzhNZl4DFlnYzUcHydnx2MnBLmXfgvmF/kqKpkxnWC7bmmMdzY9IMwgdB04t89/1O/w1cDnyilFU='
LINE_USER_ID = 'Uf92f5c6a1f7e9e3456548b5bd80fcdc4'
line_bot_api = LineBotApi(MY_CHANNEL_ACCESS_TOKEN)

# ブローカーに接続できたときの処理
def on_connect(client, userdata, flag, rc):
    print('[test_MQTT.py] Connected with result code ' + str(rc))  # 接続できた旨表示
    client.subscribe('home_IoT/watering_system', 1)  # subするトピックを設定 

# ブローカーが切断したときの処理
def on_disconnect(client, userdata, flag, rc):
    if  rc != 0:
        print('[test_MQTT.py] Unexpected disconnection.')
        
def on_message(client, userdata, msg):
    # メッセージ受け取り
    get_msg = msg.payload.decode('utf-8')
    print('[test_MQTT.py] get message {}'.format(get_msg))
    
    # 信号送信処理
    if get_msg == 'on':
        ledOn(1, GPIO_LED)
        
# MQTTの接続設定
client = mqtt.Client()                 # クラスのインスタンス(実体)の作成
client.on_connect = on_connect         # 接続時のコールバック関数を登録
client.on_disconnect = on_disconnect   # 切断時のコールバックを登録
client.on_message = on_message         # メッセージ到着時のコールバック

client.username_pw_set("token:token_egIy11cZsQCilvSa") 
client.tls_set("/home/pi/Documents/watering_system/mqtt.beebotte.com.pem")
client.connect("mqtt.beebotte.com", 8883, 60)


client.loop_start()
# line_bot_api.broadcast(TextSendMessage(text='this is test message'))while True:
    while True:
        result = sensor.read()
        if result.is_valid():
            break
    line_msg = "Temperature: %-3.1f C" % result.temperature
#     line_bot_api.broadcast(TextSendMessage(text=line_msg))
    line_bot_api.push_message(LINE_USER_ID, TextSendMessage(text=line_msg))
    time.sleep(10)
    