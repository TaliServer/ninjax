from django.shortcuts import render, HttpResponse

# Create your views here.

def test(request):
    return HttpResponse("<h1>How did you get here?</h1><br>How did <i>we</i> get here?")

def tut_home(request):
    return render(request, "tut-home.html")

def home(request):
    return render(request, "home.html")