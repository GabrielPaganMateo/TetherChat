from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("HomePage")

def index(request):
    return HttpResponse("Still Index")

def detail(request):
    return HttpResponse("You're looking at question")

def chat(request):
    return HttpResponse("Let's chat!")