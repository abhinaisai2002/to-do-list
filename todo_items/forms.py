from django import forms
from django.db import models
from . models import Items

class AddForm(forms.ModelForm):
    
    class Meta:
        model = Items
        fields=['title','description',]