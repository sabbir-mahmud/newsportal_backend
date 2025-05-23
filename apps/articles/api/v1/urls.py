from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.articles.api.v1 import views

router = DefaultRouter()
router.register("articles", views.ArticleModelView, basename="articles")
router.register("profiles", views.ProfileModelView, basename="profiles")


urlpatterns = [
    path("", include(router.urls)),
]
