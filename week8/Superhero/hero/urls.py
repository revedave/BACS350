from django.views.generic import RedirectView
from django.urls.conf import include, include
from django.contrib import admin
from django.urls import path

from hero.views import HeroView, HeroDeleteView, HeroDetailView, HeroListView, HeroCreateView, HeroUpdateView

urlpatterns = [

    path('',                   HeroListView.as_view(),    name='hero_list'),
    path('<int:pk>',           HeroDetailView.as_view(),  name='hero_detail'),
    path('add',                HeroCreateView.as_view(),  name='hero_add'),
    path('<int:pk>/',          HeroUpdateView.as_view(),  name='hero_edit'),
    path('<int:pk>/delete',    HeroDeleteView.as_view(),  name='hero_delete'),

]