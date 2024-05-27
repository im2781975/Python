#urls
from django.urls import path
from. import views
urlpatterns = [
    path('courses/',views.courses),
    path('feedback/',views.feedback),
    ]
#view
from django.shortcuts import render
from django.http import HttpResponse
def courses(request):
    return HttpResponse("This is courses page")
def feedback(request):
    return HttpResponse("This is feedback page")
