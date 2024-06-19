from rest_framework import serializers
from funko_api.models import Funko, User, Libro

class FunkoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funko
        fields = ['name', 'number', 'collection', 'is_backlight']

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ['title', 'author', 'editorial']