from django.urls import path
from . import views

urlpatterns = [
    path('home',views.homepageview,name="home"),
    path('about',views.aboutpageview,name="about"),
    path('contact',views.contactpageview,name="contact"),
    path('',views.formpageview,name="form"),
    path('formprocess',views.process,name="formprocess"),
    path('dataList',views.DataList.as_view(),name='data'),
]