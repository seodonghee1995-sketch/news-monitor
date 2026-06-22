name: News Monitor
on:
  schedule:
    - cron: '0 * * * *' # 매시간 0분에 실행
  workflow_dispatch: # 수동으로도 테스트 가능하게 함

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install feedparser requests
      - name: Run script
        run: python monitor_news.py
