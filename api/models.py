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