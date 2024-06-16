from django import forms
from Pokemon.models import Pokemon

class PokemonForm(forms.ModelForm):

    class Meta:
        model = Pokemon
        fields = [
            'name',
            'number',
            # 'type',
            # 'subtype',
            # 'generation',
        ]