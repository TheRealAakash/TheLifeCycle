from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return render(request=request, template_name="main/home.html")


def aboutpage(request):
    return render(request=request, template_name="main/about.html")


def examplespage(request):
    return render(request=request, template_name="main/examples.html")
