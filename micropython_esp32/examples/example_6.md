---
layout: page
title: Лабораторная работа №6 "Работа с BLE"
parent: "Разработка программного обеспечения на MicroPython"
permalink: /micropython_esp32/example/lr_6/
---


``` python
import bluetooth
import time

class BLEPeripheral:
    def __init__(self, name="ESP32_BLE"):
        self.name = name
        self.ble = bluetooth.BLE()
        self.ble.active(True)

        # Определяем UUID сервиса и характеристики
        self.service_uuid = bluetooth.UUID(0x180C)  # UUID сервиса
        self.char_uuid = bluetooth.UUID(0x2A56)  # UUID характеристики

        # Определяем сервис с одной характеристикой (чтение и уведомления)
        self.service = (
            self.service_uuid, [
                (self.char_uuid, bluetooth.FLAG_READ | bluetooth.FLAG_NOTIFY)
            ],
        )

        # Регистрируем сервис и получаем handle характеристики
        ((self.char_handle,),) = self.ble.gatts_register_services([self.service])

        # Флаг подключения
        self.connected = False

        # Устанавливаем обработчик событий
        self.ble.irq(self.ble_irq)

        # Запускаем рекламу BLE
        self.advertise()

    def ble_irq(self, event, data):
        if event == 1:  # Подключение
            self.connected = True
            print("Устройство подключено")

        elif event == 2:  # Отключение
            self.connected = False
            print("Устройство отключено")
            self.advertise()  # Перезапуск рекламы

    def advertise(self):
        # Простейший рекламный пакет с именем устройства
        name_bytes = self.name.encode()
        adv_payload = bytearray([2, 0x01, 0x06, len(name_bytes) + 1, 0x09]) + name_bytes
        self.ble.gap_advertise(100, adv_payload)

    def send_data(self, data):
        if self.connected:  # Проверяем подключение перед отправкой
            try:
                self.ble.gatts_write(self.char_handle, data)
                self.ble.gatts_notify(0, self.char_handle)  # Отправка данных клиенту
                print("Отправлено:", data)
            except OSError as e:
                print("Ошибка отправки:", e)

ble = BLEPeripheral(
    name="ESP32"
)

while True:
    temp = int(time.time() % 1000)  # Данные, которые будем отправлять
    ble.send_data(b"Data: %d" % temp)  # Отправка данных
    time.sleep(2)
```