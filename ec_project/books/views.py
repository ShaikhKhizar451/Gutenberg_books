from django.shortcuts import render
from rest_framework import generics
from .models import all_book
from .serializers import BookSerializer
from .filters import BookFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination



# Create your views here.
class BookListAPIView(generics.ListAPIView):
    queryset = all_book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
    pagination_class = PageNumberPagination
