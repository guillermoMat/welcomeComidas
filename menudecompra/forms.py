from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'product_name', 'description', 'photo', 'price']
        widgets = {
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }
        