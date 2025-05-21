from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from apps.articles.api.base.serializers import (
    ArticleGETSerializer,
    BaseArticleSerializer,
)
from apps.articles.models import Article
from apps.core.utils.paginator import StandardPagination


class BaseArticleModelView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Article.objects.all()
    serializer_class = BaseArticleSerializer
    pagination_class = StandardPagination

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ArticleGETSerializer
        return super().get_serializer_class()
