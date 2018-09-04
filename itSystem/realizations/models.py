from django.db import models
from django.utils.text import slugify
# Create your models here.
class Realization(models.Model):
    title = models.CharField(max_length=64)
    image = models.URLField(max_length=256)
    link = models.URLField(max_length=256)
    description = models.TextField(max_length=1024)
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Realization, self).save(*args, **kwargs)
