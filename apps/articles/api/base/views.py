from django.db.models import Q
from rest_framework import status, viewsets
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from apps.articles.api.base.serializers import (
    ArticleGETSerializer,
    BaseArticleSerializer,
    BaseProfileSerializer,
    ProfileGETSerializer,
)
from apps.articles.models import Article, Profile
from apps.core.utils.paginator import StandardPagination


class BaseArticleModelView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Article.objects.all()
    serializer_class = BaseArticleSerializer
    pagination_class = StandardPagination

    def get_queryset(self):
        search = self.request.query_params.get("search", None)
        category = self.request.query_params.get("category", None)
        country = self.request.query_params.get("country", None)
        source = self.request.query_params.get("source", None)

        if (
            self.request.user.is_authenticated
            and not search
            and not category
            and not country
            and not source
        ):
            preferences = self.request.user.profile
            country_preferences = preferences.country_preferences.values_list(
                "id", flat=True
            )
            source_preferences = preferences.source_preferences.values_list(
                "id", flat=True
            )
            category_preferences = preferences.category_preferences.values_list(
                "id", flat=True
            )
            return Article.objects.filter(
                Q(country__in=country_preferences),
                Q(source__in=source_preferences),
                Q(categories__in=category_preferences),
            )

        if search:
            return Article.objects.filter(
                Q(title__icontains=search)
                | Q(description__icontains=search)
                | Q(source__name__icontains=search)
                | Q(country__name__icontains=search)
            ).distinct()

        queryset = super().get_queryset()

        if category:
            queryset = queryset.filter(categories__id=category)
        if country:
            queryset = queryset.filter(country__id=country)
        if source:
            queryset = queryset.filter(source__id=source)

        return queryset

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ArticleGETSerializer
        return super().get_serializer_class()


class BaseProfileModelView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = BaseProfileSerializer
    pagination_class = StandardPagination

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return ProfileGETSerializer
        return super().get_serializer_class()

    def retrieve(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)
