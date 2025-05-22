from django.contrib.auth import get_user_model
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.articles.models import Profile
from apps.core.models import Category, Countries, Source

User = get_user_model()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if not created:
        return

    profile = Profile.objects.create(user=instance)

    countries = Countries.objects.filter(code__icontains="nz")
    sources = Source.objects.filter(
        Q(name__icontains="bbc news") | Q(name__icontains="cnn")
    )
    categories = Category.objects.filter(
        Q(name__icontains="car") | Q(name__icontains="automobile")
    )
    profile.country_preferences.set(countries)
    profile.source_preferences.set(sources)
    profile.category_preferences.set(categories)
