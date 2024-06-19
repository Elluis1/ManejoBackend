from rest_framework import serializers
from Pokemon.models import Pokemon, Trainer

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = [
            'name',
            'number',
            'generation',
            'type',
            'subtype'
                  ]

#Terminado