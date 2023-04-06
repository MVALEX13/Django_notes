# library used to ask the server to display an html page on the screen
from django.shortcuts import render

# utilisation et traitement des formulaires avec Django
from django import forms


### Global variables
# we use pointer
username = ["not connected"]

# Django way to deal with form
class LoginForm(forms.Form):
    username = forms.CharField(label="username")


# action realised by the server when the user arrives on the app (without specify any app functionnality)
def default(request):
    # This function returns the default page when the user connects to the application. But the default page is also returned when the user has submitted the form
    # In order to identify this case we check if the method is POST. If the method is POST, it then means that we are dealing with the second scenario, the default page will
    # be displayed because the user has submitted the form.
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        # manifestement la class Form de Django dispose d'un constructeur qui permet d'initialiser une classe à partir d'une requête
        form_sent_by_user = LoginForm(request.POST)

        # for some reason LoginForm.is_valid() must be called first so that the cleaned_data exists
        form_sent_by_user.is_valid()

        username[0] = form_sent_by_user.cleaned_data["username"]

        # we have to use pointer to avoid "local variable referenced before assignment" error 
        #  username[0] = "connected"
    return render(request, "application1/index_default.html",
                {"username": username[0]})

# action realised by the server when the user selects the 1st functionnality
def func1(request):
    return render(request,"application1/index.html",{"ind_func":1})

# action realised by the server when the user selects the 2nd functionnality
def func2(request):
    return render(request,"application1/index.html",{"ind_func":2})

def form(request):
    return render(request, "application1/form.html",{
        "form" : LoginForm()
    })

