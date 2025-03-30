from django.http import HttpResponse 
from django.http import JsonResponse 
from django.shortcuts import render

def About_page(request):
    return HttpResponse("Hello welcome to django") 
def home(request):
    data = {"city":"Chittor"}
    return JsonResponse(data) 
def Frontend(request):
    return render(request, "home.html") 
def Story(request):
    return render(request,"about.html") 
def Product(request):
    return render(request,"products.html")
def Products(request):
    return render(request,"product-detail.html")