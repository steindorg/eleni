from django.db import models
from PIL import Image
#from thumbs import ImageWithThumbsField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, SmartResize
from embed_video.fields import EmbedVideoField
from django.core.urlresolvers import reverse
from django_thumbs.db.models import ImageWithThumbsField
import os


class Photo(models.Model):
    title = models.CharField(max_length=30)
    photo =models.ImageField(upload_to='photos')
    photo_thumbnail = ImageSpecField(
        source='photo',
        processors=[SmartResize(550, 400)],
        format='JPEG',
        options={'quality': 1000}
        )

    photo_thumbnail_home_view = ImageSpecField(
        source='photo',
        processors=[SmartResize(290, 190)],
        format='JPEG',
        options={'quality': 1000}
        )
    photo_thumbnail_pro_details = ImageSpecField(
        source='photo',
        processors=[SmartResize(442, 300)],
        format='JPEG',
        options={'quality': 1000}
        )
    



    def __str__(self):
        return self.title
    

    def image_img(self):
        if self.photo:
            return u'<img src="%s" width="100" height"100"/>' % self.photo.url
        else:
            return '(No image found)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

    @property
    def filename(self):
        return os.path.basename(self.photo.name)

class Video_Link(models.Model):
    title = models.CharField(max_length=30)
    video = EmbedVideoField(verbose_name='My video',
                            help_text='This is a help text')

    def __str__(self):
        return self.title


    @property
    def filename(self):
        return os.path.basename(self.video.name)

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'pk': self.pk})


class Project(models.Model):
    PROJECT_TYPE = (
        ('Theatre', 'Theatre'),
        ('Film', 'Film'),
        ('Tv', 'Tv'),
        ('Various', 'Various')
    )
    title = models.CharField(max_length=30)
    description_box1 = models.TextField(blank=True)
    description_box2 = models.TextField(blank=True)
    role1 = models.CharField(max_length=60, blank=True)
    role2 = models.CharField(max_length=60, blank=True)
    role3 = models.CharField(max_length=60, blank=True)
    role4 = models.CharField(max_length=60, blank=True)
    role5 = models.CharField(max_length=60, blank=True)
    role6 = models.CharField(max_length=60, blank=True)
    role7 = models.CharField(max_length=60, blank=True)
    role8 = models.CharField(max_length=60, blank=True)
    role9 = models.CharField(max_length=60, blank=True)
    preview_date = models.DateField()
    project_type = models.CharField(max_length=7, choices=PROJECT_TYPE)
    photos = models.ManyToManyField(Photo)
    
    videos = models.ManyToManyField(Video_Link, blank=True)
    def __str__(self):
        return self.project_type



class Link(models.Model):
    title = models.CharField(max_length=30)
    url = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class About_detail(models.Model):
    title = "About"
    description_box1 = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos')
    about_photo_thumbnail = ImageSpecField(
        source='photo',
        processors=[SmartResize(500, 500)],
        format='JPEG',
        options={'quality': 100}
        )
    

    class Meta:
        verbose_name = "About_detail"



    def __str__(self):
        return self.title

class Contact_info(models.Model):
    title = "Contact info"
    email = models.CharField(max_length=60, blank=True)
    phone = models.CharField(max_length=60, blank=True)
    additional_1 = models.CharField(max_length=60, blank=True)
    additional_2 = models.CharField(max_length=60, blank=True)

	