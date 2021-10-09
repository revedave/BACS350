from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Superhero

class HeroView(RedirectView):
    url = '/hero/'

class HeroListView(ListView):
    template_name = 'hero_list.html'
    model = Superhero


class HeroDetailView(DetailView):
    template_name = 'hero_detail.html'
    model = Superhero

class HeroCreateView(CreateView):
    template_name = "hero_add.html"
    model = Superhero
    fields = ['name', 'identity', 'description', 'strength', 'weakness']

class HeroUpdateView(UpdateView):
    template_name = "hero_edit.html"
    model = Superhero
    fields = ['name', 'identity', 'description', 'strength', 'weakness']


class HeroDeleteView(DeleteView):
    tempplate_name = 'hero_delete.html'
    model = Superhero
    fields = ['name', 'identity', 'description', 'strength', 'weakness']