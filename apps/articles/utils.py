from django.conf import settings
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware
from newsapi import NewsApiClient

from apps.articles.models import Article
from apps.core.models import Author, Category, Countries, Source

api = NewsApiClient(api_key=settings.NEWS_API_KEY)


def store_articles(article_data, country_id, category_id):
    try:
        url = article_data.get("url")
        if not url:
            print("invalid article")
            return

        if Article.objects.filter(url=url).exists():
            print(f"already exists")
            return

        published_at = article_data.get("publishedAt")
        if published_at:
            published_at = parse_datetime(published_at)
            if published_at and not published_at.tzinfo:
                published_at = make_aware(published_at)
        else:
            published_at = timezone.now()

        source_data = article_data.get("source", {})
        source_name = source_data.get("name")
        source = None
        if source_name:
            source, _ = Source.objects.get_or_create(name=source_name)

        author_name = article_data.get("author")
        author = None
        if author_name:
            author, _ = Author.objects.get_or_create(name=author_name)

        article = Article.objects.create(
            title=article_data.get("title", "")[:500],
            description=article_data.get("description"),
            content=article_data.get("content"),
            url=url,
            url_to_image=article_data.get("urlToImage"),
            published_at=published_at,
            source=source,
            author=author,
            country_id=country_id,
        )

        article.categories.add(category_id)

        print(f"article stored")
    except Exception as e:
        print(f"error: {e}")


def get_news():
    countries = Countries.objects.values_list("id", "code")
    categories = Category.objects.values_list("id", "name")

    for country_id, country_code in countries:
        for category_id, category_name in categories:
            try:
                results = api.get_top_headlines(
                    country=country_code,
                    category=category_name.lower(),
                    page_size=100,
                )

                articles = results.get("articles", [])
                for article in articles:
                    store_articles(article, country_id, category_id)

            except Exception as e:
                print(f"error  {country_code}/{category_name}: {e}")
