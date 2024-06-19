from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token

from funko_api.models import Funko, Libro
from funko_api.serializers import FunkoSerializer, LibroSerializer
from funko_api.forms import FunkoForm

# Create your views here.

def get_all_funkos():
    funkos = Funko.objects.all().order_by('number')
    funkos_serialisers = FunkoSerializer(funkos, many=True)
    return funkos_serialisers.data

def get_all_libros():
    libros = Libro.objects.all().order_by('title')
    libros_serialisers = LibroSerializer(libros, many=True)
    return libros_serialisers.data

def index(request):
    funkos = get_all_funkos()
    return render(request, 'index.html', {'funkos': funkos})

def funkos_rest(request):
    funkos = get_all_funkos()
    return JsonResponse(funkos, safe=False)

def libros_rest(request):
    libros = get_all_libros()
    return JsonResponse(libros, safe=False)

def add_funko_view(request):
    if request.method == "POST":
        funko_form = FunkoForm(request.POST)
        if funko_form.is_valid():
            funkos = funko_form.save()
            return HttpResponseRedirect('/')
    if request.method == 'GET':
        funko_form = FunkoForm()
        csrf_token = get_token(request)
        html_form = f"""
            <form method="post">
                {funko_form.as_p()}
                <button type="submit">Submit</button>
            </form>
        """
    return HttpResponse(html_form)
    # else:
    #     pass
    
    # return(request, 'funko_form.html', {'job_form': job_form, 'skill_form'})
