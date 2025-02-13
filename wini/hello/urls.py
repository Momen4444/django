from django.urls import path
from . import views

urlpatterns=[
    path("",views.about,name="about"),
    path("<str:name>",views.home,name="home")
]