from django.contrib import admin

from apps.core.models import Category, Countries, Source

# Register your models here.
admin.site.register(Countries)
admin.site.register(Source)
admin.site.register(Category)
