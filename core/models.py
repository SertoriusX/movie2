from django.db import models

# Create your models here.
class movie(models.Model):

    iamge = models.URLField(blank=False, null=True)
    quality = models.CharField(max_length=255)
    year = models.IntegerField(blank=False, null=True)
    name= models.CharField(max_length=255)
    nota= models.CharField(max_length=255)
    image_imbd=models.URLField(blank=False, null=True)
    tags =models.ManyToManyField('Tag',related_name='tags')
    create_data=models.DateTimeField(auto_now_add=True)
    time=models.CharField(max_length=255)
    video=models.URLField(blank=False, null=True)
    description=models.TextField(blank=False, null=True)
    moviess = models.FileField(upload_to='uploads/')
    subtitle = models.FileField(upload_to='uploads')

    slug = models.SlugField(blank=False, null=True)


class Tag(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title

class lastmovie(models.Model):

    iamge = models.URLField(blank=False, null=True)
    quality = models.CharField(max_length=255)
    year = models.IntegerField(blank=False, null=True)
    name= models.CharField(max_length=255)
    nota= models.CharField(max_length=255)
    image_imbd=models.URLField(blank=False, null=True)
    tags =models.ManyToManyField('Tag_s',related_name='tags')
    create_data=models.DateTimeField(auto_now_add=True)
    time=models.CharField(max_length=255)
    slug = models.SlugField(blank=False, null=True)


class Tag_s(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.TextField()