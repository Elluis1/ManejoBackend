from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.views.generic import CreateView

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

class NewPokemonView(CreateView):
    form_class = PokemonForm
    template_name = 'form_pokemon.html'
    success_url = '/'

# class NewUserView(CreateView):
#     form_class = TrainerForm
#     template_name = 'form_user.html'
#     success_url = '/index_user'

# def add_pokemon_view(request):
    


# def add_pokemon_view(request):
#     if request.method == "POST":
#         pokemon_form = PokemonForm(request.POST)
#         if pokemon_form.is_valid():
#             pokemons = pokemon_form.save()
#             return HttpResponseRedirect('/')
#     if request.method == 'GET':
#         pokemon_form = PokemonForm()
#         csrf_token = get_token(request)
#         html_form = f"""
#             <form method="post">
#                 { % csrf_token % }
#                 {pokemon_form.as_p()}
#                 <button type="submit">Submit</button>
#             </form>
#         """
#     return HttpResponse(html_form)