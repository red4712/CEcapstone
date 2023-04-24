from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListPost.as_view()),
    path('<int:pk>/', views.DetailPost.as_view()),
    path('test/', views.ListGet.as_view()),
    path('test/<int:pk>/', views.DetailGet.as_view()),
            # 질문
    path('Question/', views.QuestionPost.as_view()),
    path('Question/<int:pk>/', views.QuestionDetail.as_view()),

        # 댓글
    path('Answer/', views.AnswerPost.as_view()),
    path('Answer/<int:pk>', views.AnswerDetail.as_view()),
    
    path('User/', views.UserPost.as_view()),
]