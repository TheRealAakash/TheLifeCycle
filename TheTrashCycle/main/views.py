from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from .apps import MainConfig
from django.conf import settings
from django.core.files.storage import default_storage


# class call_model(APIView):
#
#     def get(self,request):
#         if request.method == 'POST':
#
#             # sentence is the query we want to get the prediction for
#             image = request.POST['filename']
#
#             # predict method used to get the prediction
#             response = classifier.get_pred(image, MainConfig.type_model)
#
#             # returning JSON response
#             return JsonResponse(response)


def homepage(request):
    return render(request=request, template_name="main/home.html")


def aboutpage(request):
    return render(request=request, template_name="main/about.html")


def examplespage(request):
    return render(request=request, template_name="main/examples.html")


def get_started(request):
    return render(request=request, template_name="main/get-started.html")


def cardboard(request):
    return render(request=request, template_name='main/cardboard.html')


def get_started_submit(request):
    if request.method == "POST":
        file = request.FILES["imageFile"]
        file_name = default_storage.save(file.name, file)
        file_url = default_storage.path(file_name)
        garbage_dict = {
            "paper": "Recycling paper causes 35 per cent less water pollution and 74 per cent less air pollution than making new paper. Recycling a tonne of newspaper also eliminates 3m³ of landfill. As paper decomposes in the ground it produces methane, which is a powerful greenhouse gas, thus recycling paper prevents ass much of these gasses from being produced and released into the environment, helping",
            "cardboard": "Cardboard produces Methane, a greenhouse gas as it breaks down. Thus, every bit of cardboard recycled prevents greenhouse gases escape into the atmosphere and limit global warming.",
            "biological": "Organic waste in landfills generates, methane, a potent greenhouse gas. By composting wasted food and other organics, methane emissions are significantly reduced. Compost reduces and in some cases eliminates the need for chemical fertilizers. Compost promotes higher yields of agricultural crops.",
            "metal": "Recycling scrap metal preserves natural resources that naturally occur in nature and aren't renewable. ... Additionally, producing new metals releases more greenhouse gas emissions than the recycling process does. Similarly, recycling scrap metal uses far less energy and less water than mining for ore.",
            "plastic": "Recycling one ton of plastic saves 7.4 cubic yards of landfill space. That's not to mention the discarded plastic that ends up directly in the environment, breaking down into tiny pieces to pollute our soil and water and contribute to the oceans' Great Garbage Patches.",
            "green-glass": "Glass produced from recycled glass reduces related air pollution by 20% and related water pollution by 50%. Recycling glass reduces the space in landfills that would otherwise be taken up by used bottles and jars. Using glass for recycling means there are less glass objects lying around in he landfill or bin.",
            "brown-glass": "Glass produced from recycled glass reduces related air pollution by 20% and related water pollution by 50%. Recycling glass reduces the space in landfills that would otherwise be taken up by used bottles and jars. Using glass for recycling means there are less glass objects lying around in he landfill or bin.",
            "white-glass": "Glass produced from recycled glass reduces related air pollution by 20% and related water pollution by 50%. Recycling glass reduces the space in landfills that would otherwise be taken up by used bottles and jars. Using glass for recycling means there are less glass objects lying around in he landfill or bin.",
            "clothes": "When clothes end up in landfills they create greenhouse gases, so recycling them with Planet Aid instead helps diminish the forces that contribute to climate change. Reusing the fabric in old clothes means less resources, both monetary and environmental, are wasted in growing fiber for new ones.",
            "shoes": "A simple way to combat textile's impact on the Earth is to recycle instead of throwing out clothing. ... The clothes and shoes we have collected has saved about 300-400 million pounds of CO2 from entering the atmosphere each year, which is the equivalent of taking 26,000-35,000 cars off the road.",
            "batteries": "Data Missing",
            "trash": "Ensuring that items get disposed of properly greatly helps the environment because yes."}
        return render(request=request, template_name="main/results.html",
                      context={'file_name': file_name, 'file_path': file_url, 'garbage': ["Recyclable", "Organic"],
                               'decomp_time': {"Recyclable": "varies", "Organic": "4 weeks - 12 months"}, 'explanation':garbage_dict})
    else:
        return render(request=request, template_name="main/get-started.html")

# image = plt.imread(r"D:\OneDrive\ByteKode Hackathon\TheTrashCycle\TheTrashCycle\main\static\graphics\trash.png")
# render_class_list(image)
