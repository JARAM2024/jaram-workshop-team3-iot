import requests


def send_data(temperature, humidity, umbrella_present):
    url = "http://localhost:8000/update"
    data = {
        "temperature": temperature,
        "humidity": humidity,
        "umbrella_present": umbrella_present,
    }

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # 요청 성공 여부 확인
        print('Data sent successfully:', response.json())
    except requests.exceptions.RequestException as e:
        print('Error sending data:', e)
