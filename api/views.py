from django.shortcuts import render
from rest_framework import generics
from .models import Post, Test, Question, Answer
from .serializers import PostSerializer, TestSerializer, QuestionSerializer, AnswerSerializer



class ListPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ListGet(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class DetailGet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class QuestionPost(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerPost(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
def demo(requests):
    query = Post.objects.all()
    context = {"context":query}
    return render(requests, 'demo.html', context)