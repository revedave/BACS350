from django.contrib import admin
from django.urls import path
from hero.views import HeroDetailView, HeroListView, HeroCreateView, HeroDeleteView, HeroUpdateView, HeroView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HeroView.as_view()),
    path('hero/', HeroListView.as_view(),    name='hero_list'),
    path('hero/<int:pk>', HeroDetailView.as_view(),  name='hero_detail'),
    path('hero/add', HeroCreateView.as_view(),  name='hero_add'),
    path('hero/<int:pk>/edit', HeroUpdateView.as_view(),  name='hero_edit'),
    path('hero/<int:pk>/delete', HeroDeleteView.as_view(),  name='hero_delete'),
]