from django.db import models
import uuid

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to="media", blank=True, null=True)
    image_1 = models.ImageField(upload_to="media", blank=True, null=True)
    image_2 = models.ImageField(upload_to="media", blank=True, null=True)

    def __str__(self):
        return self.name

def randon_id_generator():
    uuid.uuid4()
    return render(request,'products.html')