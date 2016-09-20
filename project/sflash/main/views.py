from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def main_view(request):
    return redirect('theory',pk=1)