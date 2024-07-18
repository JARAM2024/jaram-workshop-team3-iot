### 거리

import RPi.GPIO as GPIO
import time

def inout_setup(TRIG, ECHO):

    GPIO.setmode(GPIO.BCM)  # GPIO 번호를 BCM 모드로 설정
    GPIO.setup(TRIG, GPIO.OUT) # TRIG 핀을 출력으로 설정
    GPIO.setup(ECHO, GPIO.IN)  # ECHO 핀을 입력으로 설정
    GPIO.output(TRIG, GPIO.LOW)  # TRIG 핀을 LOW로 초기화
    print("Waiting for sensor to settle")
    time.sleep(2)  # 센서 안정화를 위해 2초 대기

def measure_distance(TRIG, ECHO):
    # TRIG 핀을 HIGH로 설정했다가 잠시 후 LOW로 설정해 초음파 펄스를 발생
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)  # 10 마이크로초 대기
    GPIO.output(TRIG, GPIO.LOW)
    
    # ECHO 핀의 HIGH 상태 지속 시간을 측정
    while GPIO.input(ECHO) == GPIO.LOW:
        pulse_start = time.time()
    
    while GPIO.input(ECHO) == GPIO.HIGH:
        pulse_end = time.time()
    
    # 펄스 지속 시간 계산
    pulse_duration = pulse_end - pulse_start
    
    # 펄스 지속 시간을 거리로 변환
    how_far = pulse_duration * 17150  # 초음파의 속도는 34300 cm/s, 거리 = 시간 * 속도 / 2
    how_far = round(how_far, 2)  # 거리 값을 소수점 두 자리로 반올림

    #거리 출력
    print(f"Distance: {how_far} cm")
    
    return how_far

def stop():
    print("Measurement stopped by User")
    GPIO.cleanup()  # GPIO 핀 초기화