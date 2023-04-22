from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class Test(models.Model):
    Testname = models.CharField(max_length=200)
    testage = models.TextField()
    tesslk = models.TextField()

class Question(models.Model):
    subject = models.CharField(max_length=200)
    modify_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField()
    imgfile = models.ImageField(null=True, upload_to="imgfile/", blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    # viewcount = models.IntegerField(default=0) 조회수

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField()
    create_date = models.DateTimeField()

class Treasure(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    point = models.IntegerField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)