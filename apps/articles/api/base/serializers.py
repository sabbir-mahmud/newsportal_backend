from rest_framework import serializers

from apps.articles.models import Article, Profile
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


class BaseProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ProfileGETSerializer(BaseProfileSerializer):
    source_preferences = BaseSourceSerializer(many=True, read_only=True)
    country_preferences = BaseCountrySerializer(many=True, read_only=True)
    category_preferences = BaseCategorySerializer(many=True, read_only=True)
