import Adafruit_DHT
import RPi.GPIO as GPIO

def setup():
    # 핀 설정1 : distance파일에서 사용
    TRIG = 14  # TRIG 핀 (출력 : 초음파를 쏘는 역할)
    ECHO = 15  # ECHO 핀 (입력 : 초음파를 받는 역할)

    # 핀 설정2 : temhum파일에서 사용
    DHT_SENSOR = Adafruit_DHT.DHT22 # DHT22 Sensor
    DHT_PIN = 4  # GPIO 핀 번호 (BCM 번호)

    # 핀 설정3 : led파일에서 사용
    Gled = 25 #Red LED PIN
    Rled = 24 #Green LED PIN

    return TRIG, ECHO, DHT_SENSOR, DHT_PIN, Gled, Rled