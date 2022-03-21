import subprocess
import paho.mqtt.client as mqtt     # MQTTのライブラリをインポート
import datetime
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

from on_led import ledOn

# global variable
GPIO_LED = 21

# ブローカーに接続できたときの処理
def on_connect(client, userdata, flag, rc):
    print('[mqtt_aircon_control.py] Connected with result code ' + str(rc))  # 接続できた旨表示
    client.subscribe('my_home/aircon_control')  # subするトピックを設定 

# ブローカーが切断したときの処理
def on_disconnect(client, userdata, flag, rc):
    if  rc != 0:
        print('[mqtt_aircon_control.py] Unexpected disconnection.')
        
def on_message(client, userdata, msg):
    # メッセージ受け取り
    get_msg = msg.payload.decode('utf-8')
    
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

client.loop_forever()                  # 永久ループして待ち続ける