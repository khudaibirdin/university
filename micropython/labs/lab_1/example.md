---
layout: page
title: Лабораторная работа №1 "Реализация ППО для МК на языке MicroPython"
parent: "Разработка программного обеспечения на MicroPython"
permalink: /micropython_esp32/example/lr_1/
---

``` python
# импорт необходимых модулей
from machine import Pin
import time

# Инициализация пина для светодиода (например, GPIO 2)
# Уточнить на какой пин настроен встроенный светодиод и указать его номер
led = Pin(13, Pin.OUT)

# постоянный цикл для непрерывной работы микроконтроллера
while True:
    led.value(1)  # Включить светодиод
    time.sleep(1)  # Подождать 1 секунду
    led.value(0)  # Выключить светодиод
    time.sleep(1)  # Подождать 1 секунду
```