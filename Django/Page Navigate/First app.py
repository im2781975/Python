#urls
from django.urls import path
from. import views
urlpatterns = [
    path('contact/',views.contact)
    path('about/',views.about)
    ]
#view
from django.shortcuts import render
from django.http import HttpResponse
def contact(request):
    return HttpResponse("This is contact page")
def about(request):
    return HttpResponse("This is about page")
