"""django_ghostpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from ghostpost.models import Post
from ghostpost import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index_view, name="home"),
    path('upvotes/', views.upvotes, name="upvotes"),
    path('downvotes/', views.downvotes, name="downvotes"),
    path('addpost/', views.add_post_view, name="addpost"),
    path('boasts/', views.boast, name="boast"),
    path('boasts/votes/', views.boast, name="boastvotes"),
    path('roasts/', views.roast, name="roast"),
    path('roasts/votes/', views.roast, name="roastvotes"),
]