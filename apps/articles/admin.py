from django.contrib import admin

from apps.articles.models import Article, Profile

admin.site.register(Article)
admin.site.register(Profile)
