---
layout: page
title: ЛР4 "Взаимодействие с внешними API-сервисами"
parent: "Разработка программного обеспечения на MicroPython"
---


# Пример кода

``` python
# импорт необходимых модулей
import urequests
import network

# параметры сети для подключения к Wi-Fi
WIFI_SSID = ''
WIFI_PASSWORD = ''

# параметры сетевого запроса
URL_PATH =  "https://www.timeapi.io/api/time/current/ip?ipAddress=" # url сервера endpoint

station = network.WLAN(network.STA_IF)

def connect_to_wifi():
    """
    Подключенние к сети Wi-Fi
    """
    if station.isconnected():
        print("Already connected")
        return

    station.active(True)
    station.connect(
        WIFI_SSID,
        WIFI_PASSWORD
    )
    while not station.isconnected():
        pass

    print("Connection successful")
    print(station.ifconfig())

def get(url_path, parameter):
    """
    Отправка GET-запроса
    """
    url = url_path + parameter
    return urequests.get(url)

connect_to_wifi()
response = get(
    url_path=URL_PATH,
    parameter=str(station.ifconfig()[0])
)

print("Error:", response.status_code) # получаем статус операции
print("Response JSON:", response.json())  # получаем ответ в формате JSON
print("Response Text:", response.text)   # получаем ответ в текстовом формате

response.close()  # Закрываем соединение
```