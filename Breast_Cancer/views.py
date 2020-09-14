from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render (request, "Breast_Cancer/index.html")