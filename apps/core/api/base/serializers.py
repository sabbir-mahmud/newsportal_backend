from rest_framework import serializers

from apps.core.models import Author, Category, Countries, Source


class BaseCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = "__all__"


class BaseSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = "__all__"


class BaseAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BaseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
