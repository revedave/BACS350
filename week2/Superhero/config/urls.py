from django.urls import path
from hero.views import HulkView, WidowView, IronView

urlpatterns = [
    path('hulk', HulkView.as_view()),
    path('black_widow', WidowView.as_view()),
    path('iron_man', IronView.as_view()),
]