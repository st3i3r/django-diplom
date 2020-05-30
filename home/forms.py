from django import forms
from .models import UserFile


class PostForm(forms.ModelForm):
    class Meta:
        widgets = {'file': forms.FileInput()}
        model = UserFile
        fields = widgets
