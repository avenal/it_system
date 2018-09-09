from django.db import models
from django.utils.text import slugify
# Create your models here.
class Realization(models.Model):
    title = models.CharField(max_length=64)
    main_image = models.URLField(max_length=256)
    second_image = models.URLField(max_length=256)
    third_image = models.URLField(max_length=256)
    short_description = models.TextField(max_length=256)
    description = models.TextField(max_length=1024)
    slug = models.SlugField(unique=False, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Realization, self).save(*args, **kwargs)

    def __str__(self):
        return 'Nazwa: %s /id:%s' % (self.title, self.pk)
