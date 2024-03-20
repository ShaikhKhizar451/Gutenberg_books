import django_filters
from .models import all_book

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = all_book
        fields = {
            'id': ['exact'],
            'language': ['exact'],
            'genre': ['exact', 'icontains'],
            'author': ['icontains'],
            'title': ['icontains'],
            # Define other fields for filtering as per your requirements
        }
