from django.urls import path
from hero.views import AntView, SpiderView, ThorView, IndexView

urlpatterns = [
    path('', IndexView.as_view()),
    path('ant-man', AntView.as_view()),
    path('spider-man', SpiderView.as_view()),
    path('thor', ThorView.as_view()),
]
