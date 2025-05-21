from rest_framework import serializers

from apps.articles.models import Article
from apps.core.api.base.serializers import (
    BaseAuthorSerializer,
    BaseCategorySerializer,
    BaseCountrySerializer,
    BaseSourceSerializer,
)


class BaseArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class ArticleGETSerializer(BaseArticleSerializer):
    source = BaseSourceSerializer(read_only=True)
    author = BaseAuthorSerializer(read_only=True)
    country = BaseCountrySerializer(read_only=True)
    categories = BaseCategorySerializer(many=True, read_only=True)
