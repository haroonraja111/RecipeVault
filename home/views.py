from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    peoples =[
            {'name' : 'Paul' , 'age' : 26 },
            {'name' : 'John' , 'age' : 27 }, 
            {'name' : 'Sarah' , 'age' : 28 },
            {'name' : 'Jane' , 'age' : 17 },
    ]

    return render(request , 'home/index.html' , context={'page' : 'Home', 'peoples' : peoples})
    

def about(request):
    context = {'page' : 'about', 'username' : 'Paul'}

    return render(request , 'home/about.html', context)          

def contact(request):
    context = {'page' : 'contact'}
    return render(request ,'home/contact.html')