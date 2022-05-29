from http import client
import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code" + str(rc))

    client.subscribe("/call")

def on_message(client, userdata, msg):
    
    m_decode = str(msg.payload.decode("utf-8", "ignore"))
    deliveryRequest = json.loads(str(m_decode))
    print(msg.topic + " " + deliveryRequest['username'] + "\n" + deliveryRequest['destination'] )

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.loop_forever()