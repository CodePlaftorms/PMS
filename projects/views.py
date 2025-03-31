from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from pathlib import Path


print(Path(__file__).resolve().parent.parent / "static")

def login(request):
    
    return render (request,"login.html")

def dashboard(request):

    return render (request,"updatedDashboard.html")

def elearning(request):

    return render (request,"Elearning.html")

def updatedkanban(request):
    
    return render (request,"updatedkaban.html")


def template(request):
    
    return render (request,"Templates.html")


def logout(request):
    
    return render (request,"Template.html")

"""
def updatedkanban(request):
    
    return render (request,"updatedkaban.html")
def updatedkanban(request):
    
    return render (request,"updatedkaban.html")


"""