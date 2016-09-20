from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

# Create your views here.
def start_junior_test(request, pk):
    request.session['result'] = 0
    return redirect('end_junior_test')

class EndJuniorTestView(TemplateView):
    template_name = 'end_junior.html'