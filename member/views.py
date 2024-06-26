from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("HAI FRIENDS")

def about(request):
    return HttpResponse("<h1>HAI FRIENDS<h1>")