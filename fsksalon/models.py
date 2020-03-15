from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone


class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = '')
    description = RichTextField(default = "this is a Description of About FSK Salon.")
    

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to = '')
    description = RichTextField(default="this is a single line details of image")

    def __str__(self):
        return self.title  

class Bridal(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='')
    description = RichTextField(default="this is a single line details of image")

    def __str__(self):
        return self.title 

class Tattoo(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='')
    description = RichTextField(default="this is a single line details of image")

    def __str__(self):
        return self.title 

class Nail(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='')
    description = RichTextField(default="this is a single line details of image")

    def __str__(self):
        return self.title 


class Hair(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to = '')
    date = models.DateTimeField(auto_now_add=True)
    short_description = RichTextField(default = "this is a dummy text")
    description = RichTextUploadingField(default = "this is a Description of About FSK Salon.")
    slug = models.SlugField()

    def __str__(self):
        return self.title
    
    def get_hair_url(self):
        return reverse("fsksalon:hair-detail", kwargs = {
            'slug' : self.slug
        })

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='')
    short_description = RichTextField(default="Blog Short Description")
    description = RichTextUploadingField(default="Blog Long Description")
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_blog_url(self):
        return reverse("fsksalon:blog-detail", kwargs = {
            'slug' : self.slug
        })
    
class Course(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='')
    short_description = RichTextField(default="Course Short Descriptions")
    description = RichTextUploadingField(default="Couuse Long Descriptions")
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_course_url(self):
        return reverse("fsksalon:course-detail", kwargs = {
            'slug' : self.slug
        })
    
class Beauty(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='')
    short_description = RichTextField(default="Course Short Descriptions")
    description = RichTextUploadingField(default="Couuse Long Descriptions")
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_beauty_url(self):
        return reverse("fsksalon:beauty-detail", kwargs = {
            'slug' : self.slug
        })