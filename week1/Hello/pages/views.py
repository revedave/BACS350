from django.shortcuts import render

from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('<h1>Hello There.</h1><p>GENERAL KENOBI</p>')

def testPageView(request):
    return HttpResponse("<h1>This is a test</h1>" + \
    "<p>I'm trying to think but nothing happens</p?")
