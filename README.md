## Get started with Django

In this file, I'll explain, the big picture of how Django works.

### 1  - Configure a virtual environnement

Personnaly I the same environnement for all of my Web project? it's located at the relative root "`../.`" from the project location.

To do so : <br />
i) create a virtual environnement, I'll call it "Web_env" : <br /> 
`$ python3 -m venv Web_env`

ii) active your virtual env <br />
`$ source ../Web_env/bin/activate`

iii) install Django (if not installed yet) : <br />
`$ pip install Django`

### 2 - Create a Django project
Django project has a special architecture, to create it you'll have to use a Django feature (except if you want to create all the project manually which I don't recommand you). <br />
`django-admin startproject PROJECT_NAME` <br />
In my case it was : <br/>
`django-admin startproject prj_discover_Django` <br />

A folder named PROJECT_NAME (prj_discover_Django in my case) must have been created. If you click on it you shall see something like this :

![project arborescence](/img/project_arborescence_creation.png "project arborescence")

Now that the project has been created we can run the server using the manage.py file created by Django. 
Your computer we’ll play the role of the server.

`$ python manage.py runserver`

if you click on the shared url you should arrive on the following page.

![django default page](/img/django_default.png "django default page") <br />

 This is the default page that is showed when your project is being hosted but has nothing implemented yet. For the moment the server hosts a project that do nothing. Django manage the hosting part for us, but obviously it will be our job to describe what app we want. In fact a Django project is **a set of apps**.

### 3 - App creation
To create a conform app we'll ask Django to create it for us using. We'll run the following command line : <br />
`$ python manage.py startapp APP_NAME` <br />
In my case I called this app "application1", so I ran : <br />
`$ python manage.py startapp application1`

For the application we want that this project displays "Welcome in Application1". When we arrive on the good url, the server misght show us this. This require an action from the server. With Django these "actions" shall be used under the shape of functions. These functions must be declared in the *application1/views.py* file.

Une première explication grossière d'une application est de considérer qu'il s'agit d'une page. Django dispose de features permettant de gérer les pages html et de facilement intégargir avec elles depuis le code qu'on rentre côté serveur. Pour cela toutes les pages html doivent être enegistrées dans un répertoire */templates/APPLICATION_NAME* qu'on doit nous même créé. De plus pour limiter la redondance Django propose de créer des modèles de fichiers .html avec des zones modifiables c'est fichier sont nommés *layout.html*.

création du répertoire pour stocker les templates :<br/> 
`$ mkdir APPLICATION_NAME/templates` <br />
`$ mkdir application1/templates/application1`

création du modèle *layout.html* : <br />

