from django.shortcuts import render
from django.http import HttpResponse

def homepageview(request):
    return render(request,"home.html",{})

def aboutpageview(request):
    return render(request,"about.html")

def contactpageview(request):
    return render(request,"contact.html")

def formpageview(request):
    return render(request,"form.html")

def process(request):
    print("Welcome")
    print(request.method)
    print(request.POST)
    a = int(request.POST['n1'])
    b = int(request.POST['n2'])
    c = a + b
    return render(request,"ans.html",{'sum':c,'n1':a,'n2':b})