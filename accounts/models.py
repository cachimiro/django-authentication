from django.db import models
from django.utils import timezone


class index_photo(models.Model):
    """
    A single Blog post
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="img", blank=True, null=True)
    image_1 = models.ImageField(upload_to="img", blank=True, null=True)
    image_2 = models.ImageField(upload_to="img", blank=True, null=True)
    image_3 = models.ImageField(upload_to="img", blank=True, null=True)
    images = models.ImageField(upload_to="img", blank=True, null=True)
    images_1 = models.ImageField(upload_to="img", blank=True, null=True)
    images_2 = models.ImageField(upload_to="img", blank=True, null=True)
    images_3 = models.ImageField(upload_to="img", blank=True, null=True)
    imagess = models.ImageField(upload_to="img", blank=True, null=True)
    imagesss = models.ImageField(upload_to="img", blank=True, null=True)
    imagessss = models.ImageField(upload_to="img", blank=True, null=True)
    imagesssss = models.ImageField(upload_to="img", blank=True, null=True)


    def __unicode__(self):
        return self.title

# Create your models here.
