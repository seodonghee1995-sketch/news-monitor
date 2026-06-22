import feedparser
import requests

# 여기 따옴표 안에 아까 복사한 토큰을 넣으세요!
# 예: MY_PUSH_TOKEN = 'ExponentPushToken[abc1234567890]'
MY_PUSH_TOKEN = '여기에_토큰을_붙여넣으세요'

# 1. RSS URL
RSS_URL = 'https://www.hankyung.com/feed/all-news'
# 2. 푸시 알림을 보낼 Expo URL
EXPO_PUSH_ENDPOINT = 'https://exp.host/--/api/v2/push/send'

def check_news():
    feed = feedparser.parse(RSS_URL)
    # 금리가 포함된 첫 번째 기사 찾기
    for entry in feed.entries[:5]: # 최신 5개만 확인
        if '금리' in entry.title:
            send_push_notification(entry.title, entry.link)
            break 

def send_push_notification(title, link):
    message = {
        'to': MY_PUSH_TOKEN,
        'title': '금리 뉴스 알림!',
        'body': title,
        'data': {'url': link},
    }
    requests.post(EXPO_PUSH_ENDPOINT, json=message)

if __name__ == "__main__":
    check_news()
