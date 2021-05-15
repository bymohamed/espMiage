import paho.mqtt.client as paho
import json
import os, sys


def on_connect(client, userdata, rc, qos):
    client.subscribe("benyamna_sensors/temp", qos=1)


def on_message(client, userdata, msg):
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #find parent directory
    from main.models import Temperature,Esp #import django model Temperature
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))   
    jsonArray = json.loads(msg.payload)
    esp, created= Esp.objects.get_or_create(mac=jsonArray["who"])
    new = Temperature(valeur=jsonArray["value"], who=esp)
    new.save()

def on_disconnect(client, userdata, rc):
    client.loop_stop(force=False)
    if rc != 0:
        print("Unexpected disconnection.")
    else:
        print("Disconnected")



client = paho.Client()
client.on_connect = on_connect
# client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)

# client.subscribe("benyamna_sensors/temp", qos=1)

