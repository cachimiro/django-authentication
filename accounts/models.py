from django.db import models
from django.utils import timezone


class index_photo(models.Model):
    """
    A single Blog post
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="img", blank=True, null=True)
    images = models.ImageField(upload_to="img", blank=True, null=True)
    imagess = models.ImageField(upload_to="img", blank=True, null=True)
    imagesss = models.ImageField(upload_to="img", blank=True, null=True)
    imagessss = models.ImageField(upload_to="img", blank=True, null=True)
    imagesssss = models.ImageField(upload_to="img", blank=True, null=True)
    foto_de_perfil = models.ImageField(upload_to="img", blank=True, null=True)


    def __unicode__(self):
        return self.title

# Create your models here.
