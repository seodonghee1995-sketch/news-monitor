import requests

MY_PUSH_TOKEN = 'ExponentPushToken[MnJZoPJzjbUXSNRFN7TqZG]'
EXPO_PUSH_ENDPOINT = 'https://exp.host/--/api/v2/push/send'

def send_test_notification():
    message = {
        'to': MY_PUSH_TOKEN,
        'title': '테스트 알림',
        'body': '알림 시스템이 정상 작동 중입니다!',
    }
    response = requests.post(EXPO_PUSH_ENDPOINT, json=message)
    print(response.json()) # 결과 확인용

if __name__ == "__main__":
    send_test_notification()
