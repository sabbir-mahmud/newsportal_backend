from apps.articles.utils import get_news
from news.celery import app


@app.task(name="news.puller")
def news_puller():
    print("Pulling news...")
    get_news()
    return "News pulled successfully"
