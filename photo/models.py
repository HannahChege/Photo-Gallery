from django.db import models
import datetime as dt

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length =30)
    image = models.ImageField(upload_to ='')
    description = models.CharField(max_length)

