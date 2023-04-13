from rest_framework import serializers
from .models import Post, Test

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