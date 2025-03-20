---
layout: page
title: Лабораторная работа №9
parent: "Разработка программного обеспечения на MicroPython"
---


# Пример кода

``` python
import network
import time
import json
import esp32

from mqtt import MQTTClient


SSID = ""
PASSWORD = ""

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)


if not sta_if.isconnected():
    print("Connecting to Wi-Fi...")
    sta_if.connect(SSID, PASSWORD)
    while not sta_if.isconnected():
        pass

print("Connected to Wi-Fi")
print("IP address:", sta_if.ifconfig()[0])

mac = ':'.join('{:02x}'.format(b) for b in sta_if.config('mac'))


MQTT_BROKER = ""
CLIENT_ID = ""
TOPIC_SUB = ""
TOPIC_PUB = ""

def on_message(topic, msg):
    print("Received message:", msg.decode())


client = MQTTClient(CLIENT_ID, MQTT_BROKER)
client.set_callback(on_message)
client.connect()


client.subscribe(TOPIC_SUB.encode())
print("Subscribed to", TOPIC_SUB)

data = {}

try:
    while True:
        client.check_msg()
        data["temperature"] = esp32.raw_temperature()
        message = json.dumps(data).encode()
        client.publish(TOPIC_PUB.encode(), message)
        print("Published:", message)

        # Пауза
        time.sleep(5)
except Exception as e:
    print("Error:", e)
finally:
    # Отключение от брокера
    client.disconnect()
```