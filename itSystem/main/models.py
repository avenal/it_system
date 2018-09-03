from django.db import models
from django.utils import timezone
# Create your models here.
class ContactModel(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=128)
    text = models.CharField(max_length=256)
    date_added = models.DateField(default=timezone.now)
    done = models.BooleanField(default=0)
