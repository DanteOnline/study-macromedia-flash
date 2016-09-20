from django.shortcuts import render
from django.views.generic.detail import DetailView
from generic.mixin import TheoryMixin
from theory.models import Theory

# Create your views here.
class TheoryDetailView(DetailView, TheoryMixin):
    model = Theory