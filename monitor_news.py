import feedparser
import requests

# 본인의 실제 토큰으로 교체하세요!
MY_PUSH_TOKEN = 'ExponentPushToken[MnJZoPJzjbUXSNRFN7TqZG]'
EXPO_PUSH_ENDPOINT = 'https://exp.host/--/api/v2/push/send'

def check_news():
    # 한국경제 최신 뉴스 RSS
    feed = feedparser.parse('https://www.hankyung.com/feed/all-news')
    
    # 키워드 검사 없이, 가장 최신 기사 1개를 가져옵니다.
    if feed.entries:
        latest_entry = feed.entries[0]
        send_push_notification(latest_entry.title, latest_entry.link)

def send_push_notification(title, link):
    message = {
        'to': MY_PUSH_TOKEN,
        'title': '경제 뉴스 실시간 알림',
        'body': title,
        'data': {'url': link},
    }
    requests.post(EXPO_PUSH_ENDPOINT, json=message)

if __name__ == "__main__":
    check_news()
