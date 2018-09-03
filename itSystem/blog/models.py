from django.db import models

# Create your models here.
class BlogEntry(models.Model):
    title = models.CharField(max_length=64)
    image = models.URLField(max_length=256)
    description = models.TextField(max_length=4096)
