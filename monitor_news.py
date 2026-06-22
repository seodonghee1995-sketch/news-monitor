import feedparser
import requests

# 본인의 토큰을 아래 따옴표 안에 꼭 넣으세요!
MY_PUSH_TOKEN = 'ExponentPushToken[MnJZoPJzjbUXSNRFN7TqZG]'
EXPO_PUSH_ENDPOINT = 'https://exp.host/--/api/v2/push/send'

# 감시할 키워드 목록
KEYWORDS = ['금리', 'AI', '반도체', '환율']

def check_news():
    feed = feedparser.parse('https://www.hankyung.com/feed/all-news')
    
    # 최신 5개 기사 확인
    for entry in feed.entries[:5]:
        # 기사 제목에 키워드 중 하나라도 포함되어 있는지 확인
        if any(keyword in entry.title for keyword in KEYWORDS):
            send_push_notification(entry.title, entry.link)
            # 중복 알림 방지를 위해 같은 기사는 한 번만 전송
            break 

def send_push_notification(title, link):
    message = {
        'to': MY_PUSH_TOKEN,
        'title': '경제 뉴스 알림!',
        'body': title,
        'data': {'url': link},
    }
    requests.post(EXPO_PUSH_ENDPOINT, json=message)

if __name__ == "__main__":
    check_news()
