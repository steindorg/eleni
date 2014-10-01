from django.db import models
from PIL import Image

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, SmartResize
from embed_video.fields import EmbedVideoField
from django.core.urlresolvers import reverse
import os

#Database structure

#Data model for photos.
# Many to many reletions with project model and about_info model
class Photo(models.Model):
    title = models.CharField(max_length=30)
    photo =models.ImageField(upload_to='photos')
    photo_thumbnail = ImageSpecField(
        source='photo',
        processors=[ResizeToFill(520, 323)],
        format='JPEG',
        options={'quality': 1000}
        )

    #photo model functions for image rendering
    photo_thumbnail_home_view = ImageSpecField(
        source='photo',
        processors=[SmartResize(306, 207)],
        format='JPEG',
        options={'quality': 1000}
        )
    photo_thumbnail_pro_details = ImageSpecField(
        source='photo',
        processors=[ResizeToFill(750, 439)],
        format='JPEG',
        options={'quality': 1000}
        )



    # functions for model display in the admin page
    def __str__(self):
        return self.title

    # function to override the admin display behaviour of images.
    # It makes the photos visable in the admin
    def image_img(self):
        if self.photo:
            return u'<img src="%s" width="100" height"100"/>' % self.photo.url
        else:
            return '(No image found)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

    #By using the @ property, functions can be used in the logic part of the
    # MVC pattern
    @property
    def filename(self):
        return os.path.basename(self.photo.name)

# Model for video links. The django Embed Video app is used
# for video display.
# Many to one relationship to project model
class Video_Link(models.Model):
    title = models.CharField(max_length=30)
    video = EmbedVideoField(verbose_name='My video',
                            help_text='This is a help text')
    # Overriding the name of the model as displayed in the admin
    def __str__(self):
        return self.title

    # function used for fetching the url pattern of video
    @property
    def filename(self):
        return os.path.basename(self.video.name)

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'pk': self.pk})


# Model for representing the artists projects
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


# Model for storing links
class Link(models.Model):
    title = models.CharField(max_length=30)
    url = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title

# Model for the artists personal information.
# One to many relations to photo model
class About_detail(models.Model):
    title = "About"
    description_box1 = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos')
    about_photo_thumbnail = ImageSpecField(
        source='photo',
        processors=[SmartResize(950, 950)],
        format='JPEG',
        options={'quality': 100}
        )

    about_photo_thumbnail_1024 = ImageSpecField(
        source='photo',
        processors=[SmartResize(430, 450)],
        format='JPEG',
        options={'quality': 100}
        )
    about_photo_thumbnail_868 = ImageSpecField(
        source='photo',
        processors=[ResizeToFill(230, 450)],
        format='JPEG',
        options={'quality': 100}
        )


    class Meta:
        verbose_name = "About_detail"



    def __str__(self):
        return self.title

#Model for contact information
class Contact_info(models.Model):
    title = "Contact info"
    email = models.CharField(max_length=60, blank=True)
    phone = models.CharField(max_length=60, blank=True)
    additional_1 = models.CharField(max_length=60, blank=True)
    additional_2 = models.CharField(max_length=60, blank=True)

