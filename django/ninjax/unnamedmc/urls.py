from django.urls import path
from . import views

urlpatterns = [
    #path("<directory after web address>", <view function in views.py>, name="<name of tab(?)>"),
    path("", views.tut_home, name="home"),
    path("test/", views.test, name="Test-page"),

]