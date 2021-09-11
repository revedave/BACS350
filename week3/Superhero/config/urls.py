
from django.contrib import admin
from django.urls import path
from django.views.generic import AntView, SpiderView, ThorView

urlpatterns = [
    path('ant-man', AntView.as_view()),
    path('spider-man', SpiderView.as_view()),
    path('thor', ThorView.as_view()),
]
