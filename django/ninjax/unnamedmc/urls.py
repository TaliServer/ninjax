from django.urls import path
from . import views

urlpatterns = [
    #path("<directory after web address>", <view function in views.py>, name="<name of tab(?)>"),
    path("", views.home, name="Home"),
    path("test/", views.test, name="Test-page"),
    path("home/", views.home, name="home"),

]