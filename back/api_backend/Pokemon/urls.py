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

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('funkos_rest/', views.funkos_rest, name='funkos_rest'),
#     path('libros_rest/', views.libros_rest, name='libros_rest'),
#     path('add_funko/', views.add_funko_view, name='add_funko'),
# ]
