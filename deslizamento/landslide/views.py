from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request, 'landslide/home.html')

def animacao1(request):
    return render(request, 'landslide/how.html')

def animacao2(request):
    return render(request, 'landslide/what.html')
def landslide(request):
    return render(request, 'landslide/landslide.html')
def landslideManaus(request):
    return render(request, 'landslide/landslideManaus.html')