from django.shortcuts import render
from django.shortcuts import redirect
from theory.models import Theory
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from main.models import Material

class MainPageView(TemplateView):
    template_name = 'index.html'

class MaterialView(ListView):
    template_name = 'material.html'
    model = Material
    paginate_by = 100

# Create your views here.
def main_view(request):
    return redirect('theory',pk=1)

def change_image_host(request):
    old_host = 'http://127.0.0.1:8000/'
    new_host = 'http://gamesflashtest.pythonanywhere.com/'
    #new_host = 'http://127.0.0.1:8000/'

    all_theory = Theory.objects.all()
    for t in all_theory:
        t.text = t.text.replace(old_host,new_host)
        t.save()
    return redirect('index')