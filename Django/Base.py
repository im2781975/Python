from django.http import HttpResponse
def home(request):
    return HttpResponse("<h1>first django prpject")
def about(request):
    return HttpResponse("Second Django project")
