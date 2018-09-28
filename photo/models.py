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


class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()
    
    def update_location(self, update):
        self.photo_location = update
        self.save()    

class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name 

class Image(models.Model):
    title = models.CharField(max_length =30)
    photographer = models.ForeignKey(Photographer)
    description = models.TextField(max_length =30)
    image = models.ImageField(upload_to = 'photos/', default='No image')
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    pub_date = models.DateTimeField(auto_now_add=True, null=True) 

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.title
    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()
    classmethod
    def get_all_images(cls):
        all_images = Image.objects.all()
        return all_images
    
    @classmethod
    def get_image_by_id(cls, id):
        an_image = Image.objects.get(id=id)
        return an_image    


    @classmethod
    def search_by_category(cls,search_term):
        photo = cls.objects.filter(category__name__icontains=search_term)
        return photo        
    @classmethod
    def filter_by_location(cls, id):
       image = Image.objects.filter(location_id=id)
       return image  
       



