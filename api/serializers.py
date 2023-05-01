from rest_framework import serializers
from .models import Post, Test, Question, Answer
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Post

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Test

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Answer
