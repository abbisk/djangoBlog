from django.db import models
from django.utils import timezone
# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=120)
    created_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

    def was_created_recently(self):
        return self.created_on >= timezone.now() - timezone.timedelta(days=1) 


class Article(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=120)
    body = models.TextField()
    draft = models.BooleanField(default=False)
    objects = models.Manager()

    def __str__(self):
        return self.title


