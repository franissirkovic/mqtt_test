import sys
import paho.mqtt.client as mqtt
from paho.mqtt.client import connack_string, error_string

def on_connect(client, userdata, rc):
    print 'Connection result:', connack_string(rc)

def on_disconnect(client, userdata, rc):
    print 'Disconnection result:', error_string(rc)

def on_subscribe(client, userdata, mid, qos):
    print 'Subscribe successful:', qos

def on_unsubscribe(client, userdata, mid):
    print 'Unubscribe successful:'

def on_message(client, userdata, message):
    print 'Received:', message.payload

def start_receiver():
    mqttc = mqtt.Client()
    mqttc.on_connect = on_connect
    mqttc.on_disconnect = on_disconnect
    mqttc.on_subscribe = on_subscribe
    mqttc.on_unsubscribe = on_unsubscribe
    mqttc.on_message = on_message
    mqttc.connect('localhost')
    mqttc.loop_start()
    mqttc.subscribe('my/topic')
    s = ''
    while 'q' != s:
        s = raw_input('Enter "q" to exit:')
    mqttc.unsubscribe('my/topic')
    mqttc.loop_stop()
    mqttc.disconnect()
    pass

if '__main__' == __name__:
    start_receiver()
