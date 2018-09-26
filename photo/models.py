from django.db import models
import datetime as dt

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length =30)
    image = models.ImageField(blank=True, manual_crop='1600*1080')
    description = models.TextField(max_length)
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey( Category)
    def __str__(self):
        return self.name
    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()
    @classmethod
    def display_images(cls):
        images= Image.object.all()
        for image in images:
            return image   
    class Meta:
        ordering = ['name']     
class Location(models.Model):
    name = models.CharField(max_length =30)
    description = models.TextField(max_length)
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length =30)
    description = models.TextField(max_length)
    def __str__(self):
        return self.name        



