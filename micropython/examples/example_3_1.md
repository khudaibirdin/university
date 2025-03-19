---
layout: page
title: Лабораторная работа №3 "Основы работы с Wi-Fi"
parent: "Разработка программного обеспечения на MicroPython"
permalink: /micropython_esp32/example/lr_3_1/
---


``` python
# импорт необходимых модулей
import network
import time

# инициализация констант
WIFI_SSID = 'ESP32_AP'
WIFI_PASSWORD = '12345678'

# Инициализация точки доступа
ap = network.WLAN(network.AP_IF)
ap.active(True)  # Включить точку доступа
ap.config(essid=WIFI_SSID, password=WIFI_PASSWORD)  # Установить имя и пароль сети

print("Точка доступа создана")
print(f"SSID: {ap.config('essid')}, Password: {ap.config('authmode')}")
print(f"IP-адрес точки доступа: {ap.ifconfig()[0]}")


# постоянный цикл для непрерывной работы микроконтроллера
while True:
    print("Ожидание подключений...")
    # Задержка для обновления списка подключенных устройств
    time.sleep(5)
    
    # Получение списка подключенных устройств
    clients = ap.status('stations')  # Возвращает список подключенных устройств
    
    if clients:
        print(f"Подключенные устройства: {len(clients)}")
        for client in clients:
            mac_address = ':'.join(['%02X' % b for b in client[0]])  # MAC-адрес в читаемом формате
            print(f"Устройство: MAC={mac_address}")
    else:
        print("Нет подключенных устройств.")
```