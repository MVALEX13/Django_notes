from django.urls import path
from . import views

urlpatterns = [
    path("", views.default, name="default"),
    path("func1/", views.func1, name="func1"),
    path("func2/", views.func2, name="func2")
]