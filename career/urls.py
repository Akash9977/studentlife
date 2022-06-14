"""studentlife URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from career import views

urlpatterns = [
    path('index/', views.index,name="index"),
    path('login/', views.login, name="login"),
    path('contract/', views.contract, name="contract"),
    path('education/', views.education, name="education"),
    path('registation/', views.registation, name="registation"),
    path('allstu/', views.allstu, name="allstu"),
    path('about/', views.about, name="about"),
    path('bank/', views.bank, name="bank"),
    path('books/', views.books, name="books"),


]
