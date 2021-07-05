from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from TypeClassifier import classifier
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from .apps import MainConfig
from django.conf import settings
from django.core.files.storage import default_storage


class call_model(APIView):

    def get(self,request):
        if request.method == 'POST':

            # sentence is the query we want to get the prediction for
            image = request.POST['filename']

            # predict method used to get the prediction
            response = classifier.get_pred(image, MainConfig.type_model)

            # returning JSON response
            return JsonResponse(response)


def homepage(request):
    return render(request=request, template_name="main/home.html")


def aboutpage(request):
    return render(request=request, template_name="main/about.html")


def examplespage(request):
    return render(request=request, template_name="main/examples.html")


def get_started(request):
    return render(request=request, template_name="main/get-started.html")

def cardboard(request):
    return render(request=request,template_name='main/cardboard.html')


def get_started_submit(request):
    if request.method == "POST":
        file = request.FILES["imageFile"]
        file_name = default_storage.save(file.name, file)
        file_url = default_storage.path(file_name)
    else:
        return render(request=request, template_name="main/get-started.html")
    image = plt.imread(r"D:\OneDrive\ByteKode Hackathon\TheTrashCycle\TheTrashCycle\main\static\graphics\trash.png")
    render_class_list(image)
    return render(request=request, template_name="main/results.html")

def render_class_list(request, image):
    # pred = classifier.get_pred(image)
    # pred = classifier.get_class(pred)
    pred = 0
    return render(request,'main/results.html',{'garbage':[[pred, "paper"]]})
