from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.core.api.v1 import views

router = DefaultRouter()
router.register("countries", views.CountryReadOnlyView, basename="countries")
router.register("sources", views.SourceReadOnlyView, basename="sources")
router.register("authors", views.AuthorReadOnlyView, basename="authors")
router.register("categories", views.CategoryReadOnlyView, basename="categories")

urlpatterns = [
    path("", include(router.urls)),
]
