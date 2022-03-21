from django.core.paginator import Paginator


def paginator_page(request, queryset):
    return Paginator(
        queryset, 10).get_page(request.GET.get('page'))
