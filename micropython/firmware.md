---
layout: page
title: Лабораторные работы
---


# Подготовительные мероприятия

* Необходимо загрузить папку Thonny Portable в удобную директорию
* Установить плагин Esptool для Thonny
* После установки нужно проверить драйвер для устройства\
Для этого подключить устройство по USB к компьютеру и в диспетчере устройств должна отобразиться позиция:
> Порты (COM и LPT)\
> Silicon Labs CP210x USB to UART Bridge (COM3)\
> или
> Порты (COM и LPT)\
> CH340 (COM3)

Если отображается, то драйвер установлен, нужно запомнить номер порта COM3
Если не отображается, то переходим к следующему шагу

* Установить драйвер соответствующий чипу на плате ESP32, из директории 
> tools/drivers/...

