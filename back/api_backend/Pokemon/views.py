from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token

from Pokemon.models import Pokemon
from Pokemon.serializers import PokemonSerializer
from Pokemon.forms import PokemonForm

# creacion de las vistas

def get_all_pokemon():
    pokemons = Pokemon.objects.all().order_by('number')
    Pokemon_serialisers = PokemonSerializer(pokemons, many=True)
    return Pokemon_serialisers.data

def index(request):
    pokemons = get_all_pokemon()
    return render(request, 'index.html', {'pokemons': pokemons})

def pokemons_rest(request):
    pokemons = get_all_pokemon()
    return JsonResponse(pokemons, safe=False)

def add_pokemon_view(request):
    if request.method == "POST":
        pokemon_form = PokemonForm(request.POST)
        if pokemon_form.is_valid():
            pokemons = pokemon_form.save()
            return HttpResponseRedirect('/')
    if request.method == 'GET':
        pokemon_form = PokemonForm()
        csrf_token = get_token(request)
        html_form = f"""
            <form method="post">
                {pokemon_form.as_p()}
                <button type="submit">Submit</button>
            </form>
        """
    return HttpResponse(html_form)