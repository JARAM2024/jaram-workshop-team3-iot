### 온습도

import Adafruit_DHT
import time

# 온습도 측정 함수
def check_temNhum(DHT_SENSOR, DHT_PIN):
    # Adafruit_DHT라이브러리 안에 있는 read_retry함수를 이용
    # 온도 습도 측정 후 humiditiy, temperature에 저장
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    # humidity와 temperature값이 측정 됨
    if ((humidity is not None) and (temperature is not None)):
        temperature_f = temperature * 1.8 + 32
        # 습도 = __%, 온도 = __°C (__°F)
        print(f"습도 = {humidity:.1f}%, 온도 = {temperature:.1f}°C ({temperature_f:.1f}°F)")
        
    # humidity와 temperature값이 측정 안 됨
    else:
        # 데이터 읽기 실패
        print("온습도 데이터 읽기 실패")
        
    return humidity, temperature