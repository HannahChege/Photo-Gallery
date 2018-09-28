from django.test import TestCase
from .models import Photographer,Location,Image,Category
import datetime as dt

# Create your tests here.
class PhotographerTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.hannah= Photographer(first_name = 'Hannah', last_name ='Njeri')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.hannah,Photographer))   
    # Testing Save Method
    def test_save_method(self):
        self.hannah.save_photographer()
        photographers = Photographer.objects.all()
        self.assertTrue(len(photographers) > 0) 
    def test_delete_method(self):
        self.hannah.save_photographer()
        self.hannah.delete_photographer()
        photographers = Photographer.objects.all()
        self.assertTrue(len(photographers) == 0) 
    def test_display_method(self):
        self.hannah.save_photographer()
        self.hannah.display_photographers()
        photographers = Photographer.objects.all()
        self.assertTrue(len(photographers) > 0) 
    def test_update_method(self):
        self.hannah.save_photographer()
        new_photographer = Photographer.objects.filter(first_name="Hannah").update(first_name="mercy")
        photographers=Photographer.objects.get(first_name="mercy")
        self.assertTrue(photographers.first_name,"mercy")           

class LocationTestClass(TestCase):
    def  setUp(self):
        self.hannah= Tag(name ='Nairobi') 
class CategoryTestClass(TestCase):
    def  setUp(self):
        self.hannah= Tag(name ='Menswear')  

class ImageTestCase(TestCase):
    # Set Up Method
    def setUp(self):
        # self.menswear = Category(category='menswear ')
        # self.menswear .save_category()

        # self.nairobi = Location(location='Nairobi')
        # self.nairobi.save_location()

        self.image = Image(name='fashion', description='mens wear', location=self.nairobi, category=self.menswears)
        self.image.save_image()
    
    def tearDown(self):
        self.image.delete_image()
        self.menswears.delete_category()
        self.nairobi.delete_location()
    
    def test_get_all_images(self):
        images = Image.get_all_images()
        self.assertTrue(len(images)>0)
    
    def test_get_image_by_id(self):
        images = Image.get_image_by_id(self.image.id)
        self.assertTrue(images == self.image)

    def test_search_image(self):
        images = Image.search_image('Sports')
        self.assertTrue(len(images)>0)
    
    def test_filter_by_location(self):
        images = Image.filter_by_location('Nairobi')
        self.assertTrue(len(images)>0)
          
                     