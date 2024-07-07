from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("HAI FRIENDS")

def about(request):
    return HttpResponse("<h1>HAI FRIENDS<h1>")

def blog_home(request):
    # return HttpResponse(" <h2> Blog Home</h2>")
    return render(request,"blog_home.html")

def blog_details(request):
    # return HttpResponse(" <h2> Blog details</h2>")
    return render(request,"blog_details.html")

def profile(request):
    # return HttpResponse("<h2> Profile</h2>")
    return render(request,"profile.html")