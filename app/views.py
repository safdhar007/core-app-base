from django.http import request
from django.shortcuts import render

# Create your views here.
def index(request):
    safdhar="safdhar"
    a={'safdhar':safdhar}
    return render(request,'index.html',{'a':a})


def upcoming(request):
    return render(request,'upcomingprojects.html')
def tasks(request):
    return render(request,'tasks.html')
def viewprojectform(request):
    return render(request,'viewprojects.html')
def acceptedprojects(request):
    return render(request,'acceptedprojects.html')

def rejected(request):
    return render(request,'rejectedprojectes.html')

def givetask(request):
    return render(request,'givetask.html')

def currenttasks(request):
    return render(request,'currenttasks.html')
    
def previoustasks(request):
    return render(request,'previoustasks.html')