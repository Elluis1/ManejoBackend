from django.contrib import admin
from django.urls import path
from . import views

# Diseño de las urls para las vistas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('pokemons_rest/', views.pokemons_rest, name='pokemons_rest'),
    path('add_pokemon/', views.NewPokemonView.as_view(), name='add_pokemon'),
]

