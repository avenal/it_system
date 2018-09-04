from django.db import models
from django.utils.text import slugify
# Create your models here.
class BlogEntry(models.Model):
    title = models.CharField(max_length=64)
    image = models.URLField(max_length=256)
    description = models.TextField(max_length=4096)
    slug = models.SlugField(unique=False, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogEntry, self).save(*args, **kwargs)

    def __str__(self):
        return 'Nazwa: %s /id:%s' % (self.title, self.pk)
