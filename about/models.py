from django.db import models

# Create your models here.


class about(models.Model):
    Titulo = models.CharField(max_length=254, default='')
    description = models.TextField()
    image = models.ImageField(upload_to="media", blank=True, null=True)

   def __unicode__(self):
        return self.title