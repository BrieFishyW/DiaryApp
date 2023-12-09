"""
URL configuration for Diary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from Diary import views
from authenticate import views as authViews
from diaryapp import views as diaryViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),

    # login views
    path('login/', authViews.loginview, name="login"),
    path('logout/', authViews.logoutview, name="logout"),

    # diary urls
    path('diary/', diaryViews.listpage, name="diary"),
    path('new/', diaryViews.newEntry, name="new"),
]
