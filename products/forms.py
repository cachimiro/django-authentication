from django import forms
from .models import Product


class ProductPostForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'image', 'image_1', 'image_2',)