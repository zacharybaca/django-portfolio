from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    bio = models.TextField()
    date = models.DateField()