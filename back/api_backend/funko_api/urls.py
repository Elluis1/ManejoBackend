from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('funkos_rest/', views.funkos_rest, name='funkos_rest'),
    path('libros_rest/', views.libros_rest, name='libros_rest'),
    path('add_funko/', views.add_funko_view, name='add_funko'),
]
