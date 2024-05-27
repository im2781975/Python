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
    return HttpResponse('''
    <h1>this is contact page <\h1>
    <a href = '/first_app/about/'>About</a>
    ''')
def about(request):
    return HttpResponse('''
    <h1>this is about page <\h1>
    <a href = '/first_app/contact/'>Contact</a>
    ''')
