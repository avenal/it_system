from django.db import models

# Create your models here.
class Realization(models.Model):
    title = models.CharField(max_length=64)
    image = models.URLField(max_length=256)
    link = models.URLField(max_length=256)
    description = models.TextField(max_length=1024)
