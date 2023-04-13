from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListPost.as_view()),
    path('<int:pk>/', views.DetailPost.as_view()),
    path('test/', views.ListGet.as_view()),
    path('test/<int:pk>/', views.DetailGet.as_view()),

    path('demo', views.demo, name="demo")
]