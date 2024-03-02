from django import forms
from .models import Imagef

class ImagefForm(forms.ModelForm):
    class Meta:
        model=Imagef
        fields=("image",)