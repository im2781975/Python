from django.http import HttpResponse
def home(request):
    return HttpResponse("<h1>first django prpject")
def about(request):
    return HttpResponse("Second Django project")

#first app
from django.contrib import admin
from django.urls import path, include
from. import views

urlpatters = [
    path('', views.home),
    path('about/',admin.site.urls)
    ]
#first project
from django.urls import path
from.  import views
urlpatters = [
    path('about/',views.home)
    path('',include('first_app.urls'))
    ]
