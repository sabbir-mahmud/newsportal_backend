from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.core.models import Author, BaseModel, Category, Countries, Source

User = get_user_model()


class Article(BaseModel):
    title = models.TextField(blank=True, null=True, verbose_name=_("Title"))
    description = models.TextField(
        blank=True, null=True, verbose_name=_("Short Description")
    )
    content = models.TextField(blank=True, null=True, verbose_name=_("Full Content"))
    url = models.URLField(unique=True, verbose_name=_("Article URL"))
    url_to_image = models.URLField(
        max_length=1000, blank=True, null=True, verbose_name=_("Image URL")
    )
    published_at = models.DateTimeField(verbose_name=_("Published At"))
    fetched_at = models.DateTimeField(
        default=timezone.now, verbose_name=_("Fetched At")
    )

    source = models.ForeignKey(
        Source,
        on_delete=models.SET_NULL,
        null=True,
        related_name="articles",
        verbose_name=_("Source"),
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="articles",
        verbose_name=_("Author"),
    )
    country = models.ForeignKey(
        Countries,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="articles",
        verbose_name=_("Country"),
    )
    categories = models.ManyToManyField(
        Category, blank=True, related_name="articles", verbose_name=_("Categories")
    )

    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))
    views = models.PositiveIntegerField(default=0, verbose_name=_("View Count"))

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
        ordering = ["-published_at"]

    def __str__(self):
        return self.title


class Profile(BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name=_("User"),
    )
    bio = models.TextField(blank=True, null=True, verbose_name=_("Biography"))

    country_preferences = models.ManyToManyField(
        Countries,
        blank=True,
        related_name="country_preferences",
        verbose_name=_("Country Preferences"),
    )
    source_preferences = models.ManyToManyField(
        Source,
        blank=True,
        related_name="source_preferences",
        verbose_name=_("Source Preferences"),
    )
    category_preferences = models.ManyToManyField(
        Category,
        blank=True,
        related_name="category_preferences",
        verbose_name=_("Category Preferences"),
    )

    def __str__(self):
        return f"{self.user.first_name}'s Profile"

    class Meta:
        ordering = ["-id"]
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
