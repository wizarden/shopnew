from django import forms
from .models import *



class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductInOrder
        fields = '__all__'

