from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from apps.core.api.base.serializers import (
    BaseAuthorSerializer,
    BaseCategorySerializer,
    BaseCountrySerializer,
    BaseSourceSerializer,
)
from apps.core.models import Author, Category, Countries, Source
from apps.core.utils.paginator import StandardPagination


class BaseCountryReadOnlyView(viewsets.ReadOnlyModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Countries.objects.all()
    serializer_class = BaseCountrySerializer
    pagination_class = StandardPagination


class BaseSourceReadOnlyView(viewsets.ReadOnlyModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Source.objects.all()
    serializer_class = BaseSourceSerializer
    pagination_class = StandardPagination


class BaseAuthorReadOnlyView(viewsets.ReadOnlyModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Author.objects.all()
    serializer_class = BaseAuthorSerializer
    pagination_class = StandardPagination


class BaseCategoryReadOnlyView(viewsets.ReadOnlyModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = BaseCategorySerializer
    pagination_class = StandardPagination
