import pycountry

from apps.core.models import Category, Countries, Source


def create_countries_from_pycountry():
    countries = list(pycountry.countries)
    created_count = 0

    for country in countries:
        code = country.alpha_2.lower()  # usually ISO 3166-1 alpha-2 in lowercase
        name = country.name

        obj, created = Countries.objects.get_or_create(
            code=code, defaults={"name": name}
        )
        if created:
            created_count += 1
            print(f"Created country: {name} ({code})")
        else:
            print(f"Country already exists: {name} ({code})")

    print(f"Total countries created: {created_count}")


def create_sources_and_categories():
    sources = [
        "BBC News",
        "CNN",
        "Al Jazeera",
        "Reuters",
        "The Guardian",
        "Fox News",
        "Bloomberg",
        "New York Times",
        "Washington Post",
        "Sky News",
        "NDTV",
        "The Hindu",
        "ABC News",
        "CNBC",
        "Associated Press",
    ]

    categories = [
        "World",
        "Politics",
        "Business",
        "Technology",
        "Health",
        "Science",
        "Sports",
        "Entertainment",
        "Environment",
        "Education",
        "Travel",
        "Food",
        "Culture",
        "Art",
        "Lifestyle",
        "Fashion",
        "Religion",
        "Economy",
        "Startups",
        "Automobile",
        "Gaming",
        "Space",
        "Security",
        "Law",
        "Finance",
        "Real Estate",
        "Photography",
        "Animals",
        "Parenting",
        "History",
        "Weather",
        "Opinion",
        "Jobs",
        "Books",
        "Comics",
        "Energy",
        "Markets",
        "Cybersecurity",
        "Artificial Intelligence",
        "Social Media",
        "Elections",
        "Public Safety",
        "Agriculture",
        "Data Science",
        "Mental Health",
        "Productivity",
        "Innovation",
        "Movies",
        "TV Shows",
        "Podcasts",
    ]

    source_objs = [
        Source(name=name)
        for name in sources
        if not Source.objects.filter(name=name).exists()
    ]
    category_objs = [
        Category(name=name)
        for name in categories
        if not Category.objects.filter(name=name).exists()
    ]

    Source.objects.bulk_create(source_objs)
    Category.objects.bulk_create(category_objs)

    print(f"{len(source_objs)} sources and {len(category_objs)} categories created.")
