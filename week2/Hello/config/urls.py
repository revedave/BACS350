from django.urls import path
from pages.views import IndexView, HomeView, AboutView

urlpatterns = [
    path('', IndexView.as_view(template_name="index.html")),
    path('home', HomeView.as_view(template_name="home.html")),
    path('about',AboutView.as_view(template_name="page.html"))
]
