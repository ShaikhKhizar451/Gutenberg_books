from rest_framework import serializers
from .models import all_book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = all_book
        fields = '__all__'

