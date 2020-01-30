from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=120)
    created_on = models.DateTimeField(auto_now_add=True)

class Article(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=120)
    body = models.TextField()
    draft = models.BooleanField(default=False)


