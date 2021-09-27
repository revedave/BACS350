from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Superhero


class HeroView(ListView):
    template_name = 'hero_list.html'
    model = Superhero


class HeroDetailView(DetailView):
    template_name = 'hero_detail.html'
    model = Superhero
