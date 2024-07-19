import requests
import json


def send_data(temperature, humidity, umbrella_present):
    url = "http://192.168.29.117:8000/update"
    data = {
        "temperature": temperature,
        "humidity": humidity,
        "umbrella_present": umbrella_present,
        "door_open": True
    }

    try:
        response = requests.post(url, data=json.dumps(data))
        response.raise_for_status()  # 요청 성공 여부 확인
        print('Data sent successfully:', response.json())
    except requests.exceptions.RequestException as e:
        print('Error sending data:', e)
