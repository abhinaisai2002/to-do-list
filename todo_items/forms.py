from django import forms
from django.db import models
from django.db.models import fields
from . models import Items

class AddForm(forms.ModelForm):
    
    class Meta:
        model = Items
        fields=['title','description']

class UpdateItemForm(forms.ModelForm):
     
    class Meta:
        model = Items
        fields = ['title','description','status']