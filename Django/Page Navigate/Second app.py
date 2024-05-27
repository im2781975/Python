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
    return HttpResponse('''
    <h1>this is courses page <\h1>
    <a href = '/second_app/feedback/'>Feedback</a>
    ''')
def feedback(request):
    return HttpResponse('''
    <h1>this is feedback page <\h1>
    <a href = '/second_app/courses/'>Feedback</a>
    ''')
