from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image

        #yesle sabai fields linxa
        fields='__all__'
        labels={'photo':''}