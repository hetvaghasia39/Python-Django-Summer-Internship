from django.shortcuts import render
from django.http import HttpResponse

def homepageview(request):
    return HttpResponse("<h1>Welcome to my app<h1>")

def aboutpageview(request):
    return HttpResponse("<h1>About<h1>")

def contactpageview(request):
    return HttpResponse("<h2>contact<h2>")