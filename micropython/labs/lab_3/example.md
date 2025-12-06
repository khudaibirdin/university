---
layout: page
title: ЛР3 "Основы работы с Wi-Fi"
parent: "Разработка программного обеспечения на MicroPython"
---


# Пример кода 1

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

# Пример кода 2

``` python
# импорт необходимых модулей
import network
import socket
import time

# Настройки Wi-Fi (укажите имя точки доступа и пароль вашей сети телефона)
WIFI_SSID = "Имя_точки_доступа"  # Укажите имя вашей точки доступа
WIFI_PASSWORD = "Пароль_точки_доступа"  # Укажите пароль

HTML_PAGE = """\
    HTTP/1.1 200 OK

    <!DOCTYPE html>
    <html>
        <head>
            <title>ESP32 Web Server</title>
        </head>
        <body>
            <h1>Привет, Имя Фамилия выполняющего!</h1>
        </body>
    </html>
"""


def connect_to_wifi():
    """
    Подключение к Wi-Fi
    """
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    
    print("Подключение к Wi-Fi...")
    while not wlan.isconnected():
        time.sleep(1)
        print("Все еще подключаемся...")
    
    print("Успешное подключение!")
    print(f"IP-адрес ESP32: {wlan.ifconfig()[0]}")
    return wlan.ifconfig()[0]


def start_web_server(ip_address):
    """
    Запуск веб-сервера
    """
    # Создаем сокет
    addr = (ip_address, 80)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(addr)
    server_socket.listen(5)
    
    print(f"Веб-сервер запущен. Перейдите в браузере по адресу: http://{ip_address}")
    
    while True:
        conn, addr = server_socket.accept()  # Ожидание подключения клиента
        print(f"Клиент подключился с адреса: {addr}")
        
        # Чтение запроса от клиента
        request = conn.recv(1024)
        print(f"Запрос клиента:\n{request.decode('utf-8')}")
        
        # Формирование HTTP-ответа с сообщением
        conn.send(HTML_PAGE.encode('utf-8'))
        conn.close()

# Основной код
try:
    ip_address = connect_to_wifi()  # Подключение к Wi-Fi
    start_web_server(ip_address)  # Запуск веб-сервера
except Exception as e:
    print("Ошибка:", e)

```