from django import forms
from .models import index_photo


class ProductPostForm(forms.ModelForm):

    class Meta:
        model = index_photo
        fields = ('title', 'content', 'image', 'images', 'imagess', 'imagesss', 'imagessss', 'imagesssss',)