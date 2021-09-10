from django.shortcuts import render
from django.views.generic.base import TemplateView

class HulkView(TemplateView):
    template_name = 'hulk.html'

class WidowView(TemplateView):
    template_name = 'black_widow.html'

class IronView(TemplateView):
    template_name = 'iron_man.html'