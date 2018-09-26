from django.db import models
import datetime as dt

# Create your models here.
class Photographer(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    
    def __str__(self):
        return self.first_name
    def save_photographer(self):
        self.save()
    def delete_photographer(self):
        self.delete()   
    @classmethod
    def display_photographers(cls):
        photographers= Photographer.objects.all()
        for photographer in photographers:
            return photographer        
    class Meta:
        ordering = ['first_name'] 

class Image(models.Model):
    title = models.CharField(max_length =30)
    description = models.TextField(max_length)
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey( Category)
    def __str__(self):
        return self.title
    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()
   @classmethod
    def search_by_title(cls,search_term):
        photo = cls.objects.filter(title__icontains=search_term)
        return photo        
      
class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name        



