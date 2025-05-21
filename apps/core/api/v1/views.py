from apps.core.api.base.views import (
    BaseAuthorReadOnlyView,
    BaseCategoryReadOnlyView,
    BaseCountryReadOnlyView,
    BaseSourceReadOnlyView,
)


class CountryReadOnlyView(BaseCountryReadOnlyView):
    pass


class SourceReadOnlyView(BaseSourceReadOnlyView):
    pass


class AuthorReadOnlyView(BaseAuthorReadOnlyView):
    pass


class CategoryReadOnlyView(BaseCategoryReadOnlyView):
    pass
