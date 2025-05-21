from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created time"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated time"))

    class Meta:
        abstract = True


class Countries(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_("country name"))
    code = models.CharField(max_length=10, unique=True, verbose_name=_("country code"))

    class Meta:
        verbose_name = _("country")
        verbose_name_plural = _("countries")

    def __str__(self):
        return self.name


class Source(BaseModel):
    name = models.CharField(max_length=100, unique=True, verbose_name=_("source name"))
    source_id = models.CharField(
        max_length=100, blank=True, null=True, verbose_name=_("Source ID (from API)")
    )
    url = models.URLField(blank=True, null=True, verbose_name=_("Source URL"))

    class Meta:
        verbose_name = _("source")
        verbose_name_plural = _("sources")

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Author Name"))
    bio = models.TextField(blank=True, null=True, verbose_name=_("Biography"))
    profile_url = models.URLField(blank=True, null=True, verbose_name=_("Profile URL"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")


class Category(BaseModel):
    name = models.CharField(
        max_length=100, unique=True, verbose_name=_("category name")
    )

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name
