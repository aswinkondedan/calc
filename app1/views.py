from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def TestFun(request):
    return HttpResponse('HELLO')

def TestAbt(request):
    return HttpResponse('<h1>HELLO</h1>')

def TestContact(request):
    return render(request,'project2.html')
    
def TestContact(request):
    return render(request,'BStrap.html')

def bootfunction(request):
    return render (request,'boot.html')
def calcfunction(request):
    return render (request,'calc.html')