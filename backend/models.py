from django.db import models
from django.urls import reverse

class News(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Sarlavha')
    
    description = models.CharField(
        max_length=255,
        verbose_name='Tavsif')
    image = models.ImageField(
        upload_to = "images/",
        default  ="imges/default.jpg"
    )
    created = models.DateField(auto_now=True)
    
    
    
    class Meta():
        verbose_name = 'Yangilik'
        verbose_name_plural = verbose_name + 'lar'
        
    def __str__(self):
        return self.title
    


class Donat(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Sarlavha')
    
    body = models.CharField(
        max_length=255,
        verbose_name='Tavsif')
    image = models.ImageField(
        upload_to = "images/",
        default  ="imges/default.jpg"
    )
    created = models.DateField(auto_now=True)
    
    class Meta():
        verbose_name = 'Hayriya'
        verbose_name_plural = verbose_name + 'lar'
        
    
    def __str__(self):
        return self.title
    
    



class Elderly(models.Model):
    name=models.CharField(
        max_length=255,
        verbose_name='Ism')
    surname = models.CharField(
        max_length=255,
        verbose_name='Familiya')
    this_born = models.IntegerField(
        default=0,
        verbose_name="Tug'ilgan yil")
    born_place = models.CharField(
        max_length=255,
        verbose_name="Tug'ilgan joy")

    image_elderly = models.ImageField(
        upload_to = "images/",
        default  ="imges/default.jpg"
    )
    
    def __str__(self):
        return self.name 
    
    
    class Meta():
        verbose_name = 'Qariya'
        verbose_name_plural= verbose_name + 'lar'
    
     
    
    
    
 
class Archive(models.Model):
    name=models.CharField(
        max_length=255,
        verbose_name='Ism')
    surname = models.CharField(
        max_length=255,
        verbose_name='Familiya')
    this_born = models.IntegerField(
        default=0,
        verbose_name="Tug'ilgan yil")
    born_place = models.CharField(
        max_length=255,
        verbose_name="Tug'ilgan joy")

    image_archive = models.ImageField(
        upload_to = "images/",
        default  ="imges/default.jpg"   
    )
    
    def __str__(self):
        return self.name 
    
    
    class Meta():
        verbose_name = 'Arxiv'
        verbose_name_plural= verbose_name + 'lar'
        
    



class VideoGalary(models.Model):
    video_link = models.CharField(max_length=255)
    video_title = models.CharField(max_length=255)
    
    
    
    class Meta():
        verbose_name = 'Video'
        verbose_name_plural = verbose_name + 'lar'


class PhotoGalary(models.Model):
    photo_title = models.CharField(max_length=255)
    photoo = models.ImageField(
        upload_to = "images/",
        default  ="imges/default.jpg" 
        
    )
    photo_date = models.DateField(auto_now=True)
    
    class Meta():
        verbose_name = 'Rasm'
        verbose_name_plural = verbose_name + 'lar'
        
        

class Comment(models.Model):
    comment_name = models.CharField(max_length=30)
    comment = models.TextField(max_length=255)
    
    class Meta():
        verbose_name = "Fikr"
        verbose_name_plural = verbose_name + 'lar'
    
    




class Partners(models.Model):
    partner_image = models.ImageField(
        upload_to = "images/",
        default  ="imges/default.jpg" 
        
    )
    partner_title = models.CharField(max_length=255)
    partner_body = models.TextField(max_length=255)
    partner_link = models.CharField(max_length=255)

    
    class Meta():
        verbose_name = 'Hamkor'
        verbose_name_plural = verbose_name + 'lar'


class Organizers(models.Model):
    organ_image = models.ImageField(
        upload_to = "images/",
        default  ="imges/default.jpg" 
        
    )
    organ_name = models.CharField(max_length=255)
    organ_position = models.CharField(max_length=255)
    organ_description = models.CharField(max_length=255)
    
    
    
    class Meta():
        verbose_name = 'Tashkilotchi'
        verbose_name_plural = verbose_name + 'lar'