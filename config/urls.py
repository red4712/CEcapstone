"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views #추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', views.HomeView.as_view(), name='home'), #추가
    path('About/', views.About.as_view(), name='About'), #추가
    path('QnA/', views.QnA.as_view(), name='QnA'), #추가
    path('Board/', views.Board.as_view(), name='Board'), #추가
    path('AR/', views.AR.as_view(), name='AR'), #추가
    path('Game/', views.Game.as_view(), name='Game'), #추가



]
