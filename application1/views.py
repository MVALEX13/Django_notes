# library used to ask the server to display an html page on the screen
from django.shortcuts import render

# action realised by the server when the user arrives on the app (without specify any app functionnality)
def default(request):
    return render(request, "application1/index_default.html")

# action realised by the server when the user selects the 1st functionnality
def func1(request):
    return render(request,"application1/index.html",{"ind_func":1})

# action realised by the server when the user selects the 2nd functionnality
def func2(request):
    return render(request,"application1/index.html",{"ind_func":2})
