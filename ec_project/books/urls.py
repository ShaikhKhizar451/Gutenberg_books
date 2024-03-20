from django.urls import path
from books.views import BookListAPIView

urlpatterns = [
    path('api/books/', BookListAPIView.as_view(), name='book-list'),
    # Define other URL patterns for additional endpoints if needed
]
