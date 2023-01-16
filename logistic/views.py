from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'logistic/home.html')

def about(request):
    return render(request, 'logistic/about.html')

def service(request):
    return render(request, 'logistic/service.html')

def contact(request):
    return render(request, 'logistic/contact.html')