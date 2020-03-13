from django import forms
from .models import index_photo


class ProductPostForm(forms.ModelForm):

    class Meta:
        model = index_photo
        fields = ('title', 'content', 'image', 'image_1', 'image_2', 'image_3', 'images', 'images_1', 'images_2', 'images_3', 'imagess', 'imagesss', 'imagessss', 'imagesssss',)