def connect_to(ssid: str, passwd: str) -> str:
    """Conecta el microcontrolador a la red indicada y retorna la IP"""
    import network
    from time import sleep

    sta_if = network.WLAN(neEDEtwork.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to network...")
        sta_if.active(True)
        sta_if.connect(ssid, passwd)
        while not sta_if.isconnected():
            print(".", end="")
            sleep(0.05)

    return sta_if.ifconfig()[0]  # Devuelve la IP como string

# Conectar al WiFi
ip = connect_to("Cooperadora Alumnos", " ")

from machine import Pin, I2C
import ssd1306
import time

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(0)
oled.text("IP",0,0)
oled.text(ip, 0, 10)
oled.show()

