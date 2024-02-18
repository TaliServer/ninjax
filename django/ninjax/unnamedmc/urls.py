from django.urls import path
from . import views

urlpatterns = [
    #path("<directory after web address>", <view function in views.py>, name="<name of tab(?)>"),
    path("", views.tut_home, name="As I walk through the valley of the shadow of death, I take a look at myself and realize there's nothing left"),
    path("test/", views.test, name="Test-page"),
    path("home/", views.home, name="home"),

]