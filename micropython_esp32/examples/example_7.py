from serial import ModbusRTU

# пины для UART
rtu_pins = (34, 35)         # (TX, RX)
# номер UART
uart_id = 0

slave_addr = 10

# инициализация устройства Modbus RTU
client = ModbusRTU(
    addr=slave_addr,    # адрес слейва
    pins=rtu_pins,      # пины UART
    baudrate=9600,      # скорость
    data_bits=8,        # количество бит данных
    stop_bits=1,        # количество стоп-бит
    parity=None,        # четность
    ctrl_pin=12,        # пин для управления направлением передачи
    uart_id=uart_id     # номер UART
)

# иниициализация регистров
register_definitions = {
    "COILS": {
        "EXAMPLE_COIL": {
            "register": 123,
            "len": 1,
            "val": 1
        }
    },
    "HREGS": {
        "EXAMPLE_HREG": {
            "register": 93,
            "len": 1,
            "val": 19
        }
    },
    "ISTS": {
        "EXAMPLE_ISTS": {
            "register": 67,
            "len": 1,
            "val": 0
        }
    },
    "IREGS": {
        "EXAMPLE_IREG": {
            "register": 10,
            "len": 1,
            "val": 60001
        }
    }
}

# use the defined values of each register type provided by register_definitions
client.setup_registers(registers=register_definitions)

while True:
    try:
        result = client.process()
    except Exception as e:
        print('Exception during execution: {}'.format(e))