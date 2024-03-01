from django.db import models

# Create your models here.
class Post(models.Model):
    username = models.CharField(max_length=100)
    created_datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.title