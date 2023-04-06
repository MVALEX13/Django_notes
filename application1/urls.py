from django.urls import path
from . import views

# Il semblerait que le nom donné à l'application dans le fichier apps.py ne soit pas suffisant, ce nom est le nom que le serverur donne à l'application.
# En revanche le nom donné à l'application par les fichiers html est indiqué au travers de la variable app_name.
# L'application a donc 2 noms, un nom donné par le serveur et un nom donné par les fichiers html, app_name sera le nom donné par les fichiers html.
app_name = "application1"

urlpatterns = [
    path("", views.default, name="default"),
    path("func1", views.func1, name="func1"),
    path("func2", views.func2, name="func2"),
    path("form", views.form, name = "form")
]