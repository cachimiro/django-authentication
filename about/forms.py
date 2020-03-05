from django import forms
from .models import about


class ProductAboutForm(forms.ModelForm):

    class Meta:
        model = about
        fields = ('Titulo', 'description', 'image',)