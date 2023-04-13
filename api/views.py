from django.shortcuts import render
from rest_framework import generics

from .models import Post, Test
from .serializers import PostSerializer, TestSerializer

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


def demo(requests):
    query = Post.objects.all()
    context = {"context":query}
    return render(requests, 'demo.html', context)