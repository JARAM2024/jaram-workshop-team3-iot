# setup.py : setup()
# temhum.py : check_temNhum()
# distance.py : inout_setup(), measure_distance(), stop()
# led.py : state(),

import temhum, distance, setup, led
import time

TRIG, ECHO, DHT_SENSOR, DHT_PIN, Gled, Rled = setup.setup()

def main():
    #핀모드 설정
    distance.inout_setup(TRIG, ECHO)
    
    try:
        while True:
            # 온습도 측정
            temhum.check_temNhum(DHT_SENSOR, DHT_PIN)
            
            # 거리 측정
            how_far = distance.measure_distance(TRIG, ECHO)

            # led 출력
            led.state(Gled, Rled, how_far)
            
            print('')
            # 1초 쉬기 
            time.sleep(1)
            
            
    except KeyboardInterrupt:
        distance.stop()

main()