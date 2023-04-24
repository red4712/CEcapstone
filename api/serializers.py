from rest_framework import serializers
from .models import Post, Test, Question, Answer
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'content',
        )
        model = Post

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'Testname',
            'testage',
            'tesslk',
        )
        model = Test

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'id',
            'subject',
            'modify_date',   
            'content', 
            'imgfile', 
            'create_date')

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Answer
