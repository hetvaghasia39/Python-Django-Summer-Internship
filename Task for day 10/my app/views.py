from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from .models import Employee, Student

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
    name  = request.POST['name']
    email  = request.POST['email']
    password = request.POST['password']
    age = int(request.POST['age'])
    phone = int(request.POST['phone'])
    dob = request.POST['dob']
    gender = request.POST['gender']
    city = request.POST['city']
    skill = request.POST['skill']
    sem = request.POST['sem']
    return render(
        request,"ans.html",{
            'myname':name,
            'myemail':email,
            'mypassword':password,
            'myage':age,
            'myphone':phone,
            'mydob':dob,
            'mygender':gender,
            'mycity':city,
            'myskill':skill,
            'mysem':sem,
        })

class DataList(ListView):
    model = Student
    template_name = 'dataList.html'